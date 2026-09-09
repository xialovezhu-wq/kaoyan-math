#!/usr/bin/env python3
"""Seal an explicitly bounded local rollout through the existing foreground writer."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
import time

import quick_intake as qi


def parser():
    p = argparse.ArgumentParser(description=__doc__, epilog=(
        'Boundaries are inclusive 1-based physical JSONL lines containing response_item/message; '
        'end must be a user message. No text matching, summaries, score writes or model calls. '
        'Artifacts JSON: {"artifacts":[{"role":"question_image","path":"/abs/a.png",'
        '"message_line":2,"block_index":1}],"missing_attachments":[{"message_line":2,'
        '"block_index":2,"reason":"original unavailable"}]}. Block indexes are zero-based. '
        'Each non-text block needs a mapping or missing declaration unless a local image path '
        'can be resolved. Unmapped local images use other_attachment. Text blocks are concatenated '
        'without inserted separators; block lengths retain the original boundaries. '
        'Repeat the identical command after failure; existing immutable stages and captures noop.'))
    for name in ('rollout', 'session-id', 'date', 'attempt-id'):
        p.add_argument('--' + name, required=True)
    p.add_argument('--formal-id', help='Known canonical GS/LA/PR ID; validated before staging')
    p.add_argument('--source-question-id', help='Exact ID printed on the source question; resolve before staging')
    p.add_argument('--source-locator', help='Stable source identity, required for a new question without a printed ID')
    p.add_argument('--start-line', required=True, type=int)
    p.add_argument('--end-user-line', '--end-line', dest='end_user_line', required=True, type=int)
    p.add_argument('--end-assistant-line', type=int,
                   help='Include the displayed write-up after the closing user message; no later user turn may be crossed')
    p.add_argument('--repo', type=Path, help='Explicit repository root; retarget all writer paths (for isolated replay)')
    p.add_argument('--solution-line', type=int, help='Exact included assistant message; save all its text verbatim as solution_text')
    p.add_argument('--artifacts-json', type=Path, help='Explicit attachment mappings/missing declarations; defaults to none')
    p.add_argument('--queue-id')
    p.add_argument('--item-id')
    p.add_argument('--score-event-id')
    p.add_argument('--score', type=int, choices=range(6), help='Validate an already recorded score; never create one')
    p.add_argument('--requested-action', choices=sorted(qi.ALLOWED_ACTIONS))
    return p


def fail(message):
    raise qi.QuickIntakeError(message)


def local_image(value):
    if isinstance(value, dict):
        value = value.get('url') or value.get('path')
    if not isinstance(value, str):
        return None
    if value.startswith('file://'):
        value = value[7:]
    p = Path(value)
    if p.is_absolute() and p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg'} and p.is_file():
        return p
    return None


def extract(args):
    raw_lines = Path(args.rollout).read_bytes().splitlines(keepends=True)
    finish = getattr(args, 'end_assistant_line', None) or args.end_user_line
    if not 1 <= args.start_line <= args.end_user_line <= finish <= len(raw_lines):
        fail('Invalid inclusive JSONL line boundaries')
    rows = [json.loads(line) for line in raw_lines[:finish]]
    sessions = [r.get('payload', {}).get('id') for r in rows if r.get('type') == 'session_meta']
    if sessions != [args.session_id]:
        fail('Rollout session identity must match exactly one session_meta')
    def message(row):
        payload = row.get('payload', {})
        return payload if row.get('type') == 'response_item' and payload.get('type') == 'message' and payload.get('role') in ('user', 'assistant') and payload.get('phase') not in ('analysis', 'reasoning') and payload.get('channel') not in ('analysis', 'reasoning') else None
    if not message(rows[args.start_line - 1]):
        fail('start-line must point to an exact user/assistant message')
    end = message(rows[args.end_user_line - 1])
    if not end or end['role'] != 'user':
        fail('end-user-line must point to an exact user message')
    if finish > args.end_user_line:
        tail = message(rows[finish - 1])
        if not tail or tail['role'] != 'assistant' or tail.get('recipient') not in (None, 'all'):
            fail('end-assistant-line must point to an exact visible assistant message')
        if any((m := message(row)) and m['role'] == 'user' for row in rows[args.end_user_line:finish]):
            fail('Cannot cross another user turn after the closing request')
    specification = json.loads(args.artifacts_json.read_text()) if args.artifacts_json else {}
    if not isinstance(specification, dict) or set(specification) - {'artifacts', 'missing_attachments'}:
        fail('Invalid artifacts JSON object')
    mappings, missing_map = {}, {}
    for field, destination in [('artifacts', mappings), ('missing_attachments', missing_map)]:
        for item in specification.get(field, []):
            key = (item.get('message_line'), item.get('block_index'))
            if key in destination or not all(type(v) is int for v in key):
                fail('Attachment requires unique integer message_line and block_index')
            if field == 'artifacts' and set(item) != {'message_line', 'block_index', 'role', 'path'}:
                fail('Artifact fields must be role, path, message_line, block_index')
            if field == 'missing_attachments' and (set(item) != {'message_line', 'block_index', 'reason'} or not isinstance(item['reason'], str) or not item['reason'].strip()):
                fail('Missing attachment requires a nonempty reason')
            destination[key] = item
    if mappings.keys() & missing_map.keys():
        fail('Attachment cannot be both present and missing')
    turns, provenance, artifacts, missing, used = [], [], [], [], set()
    solution = None
    seen_paths = set()
    def add_artifact(role, path):
        path = Path(path).expanduser()
        if not path.is_absolute() or not path.is_file() or path.is_symlink():
            fail('Artifact path must be an existing absolute regular file')
        resolved = str(path.resolve())
        if resolved not in seen_paths:
            artifacts.append({'role': role, 'path': resolved})
            seen_paths.add(resolved)
    def default_role(path):
        if path.parent.name == args.formal_id and path.stem.startswith('question_'):
            return 'question_image'
        if path.suffix.lower() == '.svg':
            return 'explanation_image'
        return 'other_attachment'
    for line_no in range(args.start_line, finish + 1):
        m = message(rows[line_no - 1])
        if not m:
            continue
        # Tool-call assistant messages are not conversation, even if they contain text.
        if m.get('recipient') not in (None, 'all'):
            if line_no in (args.start_line, args.end_user_line, args.solution_line):
                fail('Boundary/solution cannot refer to a tool-call message')
            continue
        blocks = m.get('content')
        if not isinstance(blocks, list):
            fail('Message content must be a list of typed blocks')
        texts, lengths = [], []
        for index, block in enumerate(blocks):
            key = (line_no, index)
            if not isinstance(block, dict):
                fail('Invalid message block')
            is_text = block.get('type') in ('input_text', 'output_text', 'text')
            if is_text:
                text = block.get('text')
                if not isinstance(text, str):
                    fail('Text block lacks exact text')
                texts.append(text)
                lengths.append(len(text))
                # Only references within this exact selected message are considered.
                for ref in re.findall(r'!\[[^\]]*\]\(<?([^\n)]+?)>?\)', text):
                    path = local_image(ref)
                    if path:
                        add_artifact(mappings.get(key, {}).get('role', default_role(path)), path)
                    elif key not in mappings and key not in missing_map:
                        fail(f'Unresolved image reference at line {line_no}, block {index}; provide artifacts JSON')
            if key in mappings:
                item = mappings[key]
                add_artifact(item['role'], item['path'])
                used.add(key)
            elif key in missing_map:
                missing.append(f'attachment:{line_no}:{index}: {missing_map[key]["reason"]}')
                used.add(key)
            elif not is_text:
                path = local_image(block.get('image_url') or block.get('url') or block.get('path'))
                if path:
                    add_artifact(default_role(path), path)
                else:
                    fail(f'Unresolved non-text block at line {line_no}, block {index}; provide mapping or missing reason')
        text = ''.join(texts)
        turns.append({'role': m['role'], 'text': text})
        provenance.append({'line': line_no, 'text_block_lengths': lengths,
                           'block_types': [b.get('type') for b in blocks]})
        if line_no == args.solution_line:
            if m['role'] != 'assistant':
                fail('solution-line must be an included assistant message')
            solution = text
    if used != mappings.keys() | missing_map.keys():
        fail('Attachment mapping points outside selected conversation blocks')
    if args.solution_line is not None and solution is None:
        fail('solution-line must be inside the exact selected conversation')
    return turns, provenance, artifacts, missing, solution, hashlib.sha256(b''.join(raw_lines[args.start_line-1:finish])).hexdigest()


def invoke(command, payload, directory):
    path = directory / (command + '.json')
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        getattr(qi, 'cmd_' + command.replace('-', '_'))(argparse.Namespace(payload_file=str(path)))
    return json.loads(out.getvalue())


def configure_repo(root):
    root = root.expanduser().resolve(strict=True)
    if not root.is_dir():
        fail('--repo must be an existing repository directory')
    old_root = qi.REPO_ROOT
    for name, value in list(vars(qi).items()):
        if isinstance(value, Path) and value.is_relative_to(old_root):
            setattr(qi, name, root / value.relative_to(old_root))


def resolve_identity(args):
    """Read canonical source metadata once, before extracting or staging evidence."""
    question_id = args.source_question_id
    formal_id = args.formal_id
    if question_id is not None:
        question_id = qi.require_text(question_id, 'source-question-id', max_length=200)
        qi.reject_local_absolute_paths(question_id, 'source-question-id')
        if not qi.CARDS_DIR.is_dir():
            fail('Canonical card directory unavailable; cannot classify the source ID')
        spec = importlib.util.spec_from_file_location('capture_identity_wrongnet', qi.WRONGNET_TOOL_PATH)
        if spec is None or spec.loader is None:
            fail('Canonical source metadata parser unavailable')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        matches = []
        for path in sorted(qi.CARDS_DIR.glob('*.md')):
            if not qi.CARD_ID_PATTERN.fullmatch(path.stem.split('_', 1)[0]):
                continue
            # Parse only front matter. Body examples and related questions are not identity.
            with path.open(encoding='utf-8') as handle:
                first = handle.readline()
                if first.strip() != '---':
                    fail(f'Canonical card lacks front matter: {path.name}')
                header = [first]
                for line in handle:
                    header.append(line)
                    if line.strip() == '---':
                        break
                else:
                    fail(f'Canonical card has unclosed front matter: {path.name}')
            meta, _ = module.split_front_matter(''.join(header))
            exact = any(str(meta.get(key, '')) == question_id
                        for key in ('source_question_id', 'question_id', 'source_id'))
            source = str(meta.get('source') or '')
            # Legacy source fields mix book labels/dates with 5+ digit printed IDs.
            numeric = re.fullmatch(r'[0-9]{5,}', question_id) and re.search(
                r'(?<![A-Za-z0-9])' + re.escape(question_id) + r'(?![A-Za-z0-9])', source)
            labelled = re.search(r'(?i)(?<![A-Za-z0-9])ID\s*[:：]\s*' + re.escape(question_id)
                                + r'(?![A-Za-z0-9_-])', source)
            if exact or numeric or labelled:
                card_id = str(meta.get('id', ''))
                if not qi.CARD_ID_PATTERN.fullmatch(card_id):
                    fail(f'Matched source has invalid formal ID: {path.name}')
                matches.append(card_id)
        if len(matches) > 1:
            fail('Source question ID matches multiple formal cards: ' + ', '.join(matches))
        if matches:
            if formal_id and formal_id != matches[0]:
                fail('Source question ID conflicts with supplied formal-id')
            formal_id = matches[0]
    if not formal_id and not question_id and not args.source_locator:
        fail('Supply formal-id, source-question-id, or a stable source-locator')
    locator = args.source_locator or f'codex:{args.session_id}:math:{formal_id or "new_source:" + question_id}:{args.attempt_id}'
    qi.reject_local_absolute_paths(locator, 'source-locator')
    target = ({'kind': 'formal_card', 'formal_id': formal_id} if formal_id else
              {'kind': 'new_source', 'source_locator': locator})
    qi.normalize_target(target, None)
    return target, locator, question_id


def capture(args):
    if args.repo is not None:
        configure_repo(args.repo)
    started = time.perf_counter()
    target, locator, question_id = resolve_identity(args)
    args.formal_id = target.get('formal_id')
    turns, provenance, artifacts, missing, solution, slice_hash = extract(args)
    qi.validate_date(args.date)
    score = qi.score_reference(args.score_event_id)
    if args.score is not None and score is None:
        fail('--score requires an existing --score-event-id')
    if (args.queue_id is None) != (args.item_id is None):
        fail('queue-id and item-id must be supplied together')
    if score:
        expected = {'attempt_id': args.attempt_id, 'study_date': args.date, 'formal_id': args.formal_id}
        expected.update({k: v for k, v in [('queue_id', args.queue_id), ('queue_item_id', args.item_id), ('score', args.score)] if v is not None})
        if any(score[k] != v for k, v in expected.items()):
            fail('Requested identity/queue/item/score conflicts with recorded score')
    qi.normalize_target(target, score)  # Reject identity errors before any stage write.
    if not qi.ATTEMPT_ID_PATTERN.fullmatch(args.attempt_id):
        fail('Invalid attempt-id')
    prepare_ms = (time.perf_counter() - started) * 1000
    with tempfile.TemporaryDirectory(prefix='capture-current-math-') as temp:
        directory = Path(temp)
        if solution is not None:
            if any(a['role'] == 'solution_text' for a in artifacts):
                fail('solution-line and explicit solution_text cannot both be supplied')
            solution_path = directory / 'solution.txt'
            solution_path.write_bytes(solution.encode('utf-8'))
            artifacts.append({'role': 'solution_text', 'path': str(solution_path)})
        stage_payload = {
            'schema_version': qi.SOURCE_STAGE_SCHEMA_V2, 'package_key': args.attempt_id,
            'study_date': args.date, 'timezone': 'Asia/Shanghai',
            'source': {'source_locator': locator,
                       'session_id': args.session_id, 'formal_id': args.formal_id,
                       'capture_identity': args.attempt_id, 'queue_id': args.queue_id,
                       'item_id': args.item_id, 'score_event_id': args.score_event_id,
                       'rollout_slice_sha256': slice_hash, 'message_boundaries': provenance},
            'conversation': turns, 'artifacts': artifacts, 'missing_fields': missing,
        }
        if question_id is not None:
            stage_payload['source']['question_id'] = question_id
        stage_start = time.perf_counter()
        stage = invoke('stage-source', stage_payload, directory)
        stage_ms = (time.perf_counter() - stage_start) * 1000
        record_start = time.perf_counter()
        record = invoke('record', {
            'schema_version': qi.CAPTURE_SCHEMA_V3, 'attempt_id': args.attempt_id,
            'study_date': args.date, 'target': target, 'score_event_id': args.score_event_id,
            'requested_action': args.requested_action or ('record_wrong' if target['kind'] == 'new_source' else 'record_recurrence'), 'thread_ref': args.session_id,
            'conversation_package': {k: stage[k] for k in ('manifest_path', 'manifest_hash', 'package_sha256')},
        }, directory)
        record_ms = (time.perf_counter() - record_start) * 1000
    return {'stage_status': stage['status'], 'record_status': record['status'],
            'capture_event_id': record.get('capture_event_id') or record.get('event_id'),
            'package_id': stage['package_id'], 'manifest_path': stage['manifest_path'],
            'target_kind': target['kind'], 'formal_id': args.formal_id, 'source_question_id': question_id,
            'manifest_hash': stage['manifest_hash'], 'package_sha256': stage['package_sha256'],
            'rollout_slice_sha256': slice_hash, 'turn_count': len(turns),
            'elapsed_ms': {k: round(v, 3) for k, v in [('prepare', prepare_ms), ('stage', stage_ms),
                ('record', record_ms), ('total', (time.perf_counter() - started) * 1000)]},
            'formal_write_count': 0, 'score_write_count': 0, 'model_call_count': 0}


def main():
    try:
        if len(sys.argv) > 1 and sys.argv[1] == 'messages':
            p = argparse.ArgumentParser(description='Locate exact current-task message lines without ad-hoc extraction code')
            p.add_argument('--rollout', type=Path, required=True)
            p.add_argument('--session-id', required=True)
            p.add_argument('--limit', type=int, default=10)
            args = p.parse_args(sys.argv[2:])
            rows = [json.loads(line) for line in args.rollout.read_text().splitlines()]
            if [r.get('payload', {}).get('id') for r in rows if r.get('type') == 'session_meta'] != [args.session_id]:
                fail('Rollout session identity mismatch')
            messages = []
            for line, row in enumerate(rows, 1):
                m = row.get('payload', {})
                if (row.get('type') == 'response_item' and m.get('type') == 'message'
                    and m.get('role') in ('user', 'assistant') and m.get('recipient') in (None, 'all')
                    and m.get('phase') not in ('analysis', 'reasoning') and m.get('channel') not in ('analysis', 'reasoning')):
                    blocks = m.get('content', [])
                    text = ''.join(b.get('text', '') for b in blocks if b.get('type') in ('input_text', 'output_text', 'text'))
                    messages.append({'line': line, 'role': m['role'], 'preview': text[:90],
                                     'blocks': [b.get('type') for b in blocks]})
            print(json.dumps(messages[-max(1, min(args.limit, 100)):], ensure_ascii=False))
            return 0
        print(json.dumps(capture(parser().parse_args()), ensure_ascii=False, sort_keys=True))
    except (qi.QuickIntakeError, OSError, ValueError, TypeError) as exc:
        print(json.dumps({'status': 'error', 'error': str(exc),
                          'recovery': 'Fix the input or retry the identical command; no existing package is overwritten.'}, ensure_ascii=False))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
