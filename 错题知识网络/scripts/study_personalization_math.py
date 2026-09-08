"""Immutable native math personalization export and offline query contract."""
from __future__ import annotations

import base64
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import tempfile

import math_concept_index as native

SCHEMA = "study-personalization-math-v1"
ENTRYPOINT = "personalization/math/manifest.json"
EXPORT_ROOT = Path("错题知识网络/个人知识点索引/发布快照")


def _read_meta(conn):
    return {k: json.loads(v) for k, v in conn.execute("SELECT key,value FROM meta")}


def _identity(root, conn, meta):
    version = meta.get("version")
    epoch = root / native.STORES[5]
    formal_version = hashlib.sha256(epoch.read_bytes()).hexdigest() if epoch.is_file() else native.digest(
        list(conn.execute("SELECT path,sha256 FROM sources WHERE path LIKE '错题知识网络/错题卡/%' ORDER BY path")))
    required = {"schema", "version", "directories", "store_stamps", "coverage", "alias_problems"}
    changed = [p for p, stamp in {**meta.get("directories", {}), **meta.get("store_stamps", {})}.items()
               if native._stamp(root / p) != stamp]
    return {"status": "pending" if not required.issubset(meta) else "stale" if changed else "ready",
            "version": version, "formal_version": formal_version, "changed_sources": changed}


def current_identity(repo_root: Path) -> dict:
    """Read index metadata and known directory/hot-store stamps; never crawl cards."""
    root = Path(repo_root).resolve()
    path = root / native.INDEX
    if not path.is_file():
        return {"status": "pending", "version": None, "formal_version": None, "reason": "index_missing"}
    try:
        with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as conn:
            conn.execute("BEGIN")
            return _identity(root, conn, _read_meta(conn))
    except (sqlite3.Error, ValueError, OSError) as exc:
        return {"status": "pending", "version": None, "formal_version": None, "reason": type(exc).__name__}


def _write(path, value):
    raw = value if isinstance(value, bytes) else native.canonical(value).encode()
    if path.is_file() and path.read_bytes() == raw:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".snapshot-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def export_snapshot(repo_root: Path, output_dir: Path) -> dict:
    """Export JSON under one SQLite read transaction; never copy a live database."""
    root = Path(repo_root).resolve()
    path = root / native.INDEX
    if not path.is_file():
        raise ValueError("math_personalization_index_missing")
    with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as conn:
        conn.execute("BEGIN")
        meta = _read_meta(conn)
        identity = _identity(root, conn, meta)
        if identity["status"] != "ready":
            raise ValueError("math_personalization_index_" + identity["status"])
        source_rows = list(conn.execute("SELECT path,stamp,sha256 FROM sources ORDER BY path"))
        # Publication is maintenance, so verify all indexed source stamps here.
        if any(native._stamp(root / p) != json.loads(stamp) for p, stamp, _ in source_rows if native._hot_source(p)):
            raise ValueError("math_personalization_index_stale")
        payload = {"schema": SCHEMA, "version": identity["version"], "formal_version": identity["formal_version"],
                   "meta": {k: meta[k] for k in ("schema", "coverage", "alias_problems", "scope_notes", "require_scope_check") if k in meta},
                   "coverage": meta.get("receipt", {}).get("coverage", meta["coverage"]),
                   "concepts": {k: json.loads(v) for k, v in conn.execute("SELECT key,payload FROM concepts ORDER BY key")},
                   "lookup": list(conn.execute("SELECT name,key FROM lookup ORDER BY name,key")),
                   "records": {k: json.loads(v) for k, v in conn.execute("SELECT id,payload FROM records ORDER BY id")},
                   "membership": list(conn.execute("SELECT key,record_id FROM membership ORDER BY key,record_id")),
                   "sources": [{"path": p, "sha256": sha} for p, _, sha in source_rows]}
        # Native raw-user evidence can have a complete turn file behind the
        # selected excerpt. Export the exact referenced caches as evidence too.
        cache_prefix = "错题知识网络/个人知识点索引/source_cache/"
        review_prefix = "数学一回滚复习系统/知识点复盘/正式会话/"
        evidence_refs = {p: sha for p, _, sha in source_rows if p.startswith((cache_prefix, review_prefix))}
        def collect_cache_refs(value):
            if isinstance(value, dict):
                cache = value.get("user_turn_cache")
                if isinstance(cache, str) and cache.startswith(cache_prefix):
                    evidence_refs[cache] = value["user_turn_cache_sha256"]
                for child in value.values():
                    collect_cache_refs(child)
            elif isinstance(value, list):
                for child in value:
                    collect_cache_refs(child)
        collect_cache_refs(payload["records"])
        evidence = []
        for reference, sha in sorted(evidence_refs.items()):
            source = root / reference
            allowed_root = root / (review_prefix if reference.startswith(review_prefix) else cache_prefix)
            if source.is_symlink() or not source.resolve().is_relative_to(allowed_root.resolve()):
                raise ValueError("unsafe_native_cache_reference")
            raw = source.read_bytes()
            if hashlib.sha256(raw).hexdigest() != sha:
                raise ValueError("native_cache_evidence_hash_mismatch")
            evidence.append((reference, sha, raw))
        if _identity(root, conn, meta) != identity:
            raise ValueError("math_personalization_source_changed_during_export")
    directory = Path(output_dir).resolve()
    data_path = directory / "native-index.json"
    manifest_path = directory / "manifest.json"
    data = native.canonical(payload).encode()
    manifest = {"schema": SCHEMA, "subject": "math", "status": "ready", "version": identity["version"],
                "formal_version": identity["formal_version"], "entrypoint": ENTRYPOINT,
                "native_schema": native.SCHEMA, "native_implementation": native.IMPLEMENTATION,
                "coverage": payload["coverage"], "data_file": "native-index.json",
                "data_sha256": hashlib.sha256(data).hexdigest(), "source": "native_read_transaction_export",
                "views": ["protected", "after_attempt", "direct"]}
    extra_files = []
    for reference, sha, raw in evidence:
        relative = "sources/" + sha + "/" + Path(reference).name
        target = directory / relative
        _write(target, raw)
        extra_files.append({"source_path": str(target), "publish_path": "personalization/math/" + relative,
                            "kind": "personalization_source_evidence", "original_reference": reference,
                            "expected_sha256": sha})
    manifest["source_mappings"] = [{k: v for k, v in row.items() if k != "source_path"} for row in extra_files]
    _write(data_path, payload)
    _write(manifest_path, manifest)
    return {**identity, "manifest_path": str(manifest_path), "entrypoint": ENTRYPOINT,
            "files": [{"source_path": str(p), "publish_path": "personalization/math/" + p.name,
                       "kind": "personalization_manifest" if p == manifest_path else "personalization_native_index"}
                      for p in (manifest_path, data_path)] + extra_files}


def query_snapshot(manifest_path: Path, knowledge_points: list[str], weak_knowledge_points: list[str],
                   view: str, max_bytes: int, cursor: str = "") -> dict:
    """Query only exported JSON; no live paths, SQLite, or native resolver calls."""
    if view not in {"protected", "after_attempt", "direct"} or type(max_bytes) is not int or max_bytes < 64:
        raise ValueError("invalid view or max_bytes")
    if any(not isinstance(xs, list) or any(not isinstance(x, str) for x in xs)
           for xs in (knowledge_points, weak_knowledge_points)):
        raise ValueError("knowledge points must be string arrays")
    path = Path(manifest_path).resolve()
    manifest = json.loads(path.read_text())
    if manifest.get("schema") != SCHEMA or manifest.get("data_file") != "native-index.json":
        raise ValueError("invalid_math_personalization_manifest")
    data_path = path.parent / "native-index.json"
    if data_path.is_symlink():
        raise ValueError("snapshot_symlink_forbidden")
    data = data_path.read_bytes()
    if hashlib.sha256(data).hexdigest() != manifest["data_sha256"]:
        raise ValueError("math_personalization_snapshot_hash_mismatch")
    snapshot = json.loads(data)
    if any(snapshot[k] != manifest[k] for k in ("version", "formal_version", "schema")):
        raise ValueError("math_personalization_snapshot_version_mismatch")
    queries = list(dict.fromkeys(knowledge_points + weak_knowledge_points))
    query_hash = native.digest([knowledge_points, weak_knowledge_points, view])
    offset = 0
    if cursor:
        try:
            state = json.loads(base64.urlsafe_b64decode(cursor.encode()).decode())
        except Exception as exc:
            raise ValueError("invalid_cursor") from exc
        if state.get("version") != manifest["version"] or state.get("query") != query_hash:
            raise ValueError("cursor_query_or_version_mismatch")
        offset = state.get("offset")
        if type(offset) is not int or offset < 0:
            raise ValueError("invalid_cursor_offset")
    meta = snapshot["meta"]
    names = {}
    for name, key in snapshot["lookup"]:
        names.setdefault(name, set()).add(key)
    bad = {native.normalize(p["alias"]): p for p in meta["alias_problems"]}
    keys, weak_keys, unknown, ambiguous = set(), set(), [], []
    for query in queries:
        norm = native.normalize(query)
        if norm in bad:
            ambiguous.append({"query": query, **bad[norm]})
            continue
        found = names.get(norm, set())
        if not found:
            unknown.append(query)
        keys.update(found)
        if query in weak_knowledge_points:
            weak_keys.update(found)
    resolved, all_ids = [], set()
    for key in sorted(keys):
        concept = snapshot["concepts"][key]
        all_ids.update(concept["formal_ids"])
        resolved.append({k: v for k, v in concept.items() if k not in {"formal_ids", "source_refs"}} |
                        {"formal_count": len(concept["formal_ids"])})
    memberships = {}
    for key, rid in snapshot["membership"]:
        if key in keys:
            memberships.setdefault(rid, set()).add(key)
    def ranking(rid):
        record = snapshot["records"][rid]
        priority = record.get("retrieval_priority", {})
        day = priority.get("latest_explicit_learning_date")
        return (not native.is_personal_record(record), not bool(memberships[rid] & weak_keys),
                -int(bool(priority.get("explicit_personal_or_actual_delivery"))),
                -int(day.replace("-", "")) if day else 0, rid)
    ordered = [native._view(snapshot["records"][rid], view, resolved) for rid in sorted(memberships, key=ranking)]
    if offset > len(ordered):
        raise ValueError("invalid_cursor_offset")
    scope = {native.normalize(k): v for k, v in meta.get("scope_notes", {}).items()}
    checks = {native.normalize(k) for k in meta.get("require_scope_check", [])}
    coverage = snapshot["coverage"]
    result = {"schema": SCHEMA, "status": "ambiguous_concept" if ambiguous else "unknown_concept" if not keys else "available",
              "version": manifest["version"], "formal_version": manifest["formal_version"], "view": view,
              "source": "published_native_snapshot", "source_entrypoint": ENTRYPOINT,
              "resolved": resolved, "unknown": unknown, "ambiguous": ambiguous,
              "query_scope_notes": [{"query": q, "note": scope[native.normalize(q)], "require_scope_check": native.normalize(q) in checks}
                                    for q in queries if native.normalize(q) in scope],
              "coverage": {k: coverage[k] for k in ("expected_count", "observed_count", "missing_ids")},
              "evidence_policy": "card_association_is_not_proof_of_same_error; current_attempt_is_authoritative; no_mastery_inference",
              "order": "personal_before_material;weak_keys_first;native_priority_and_date_then_id",
              "total": len(ordered), "personal_record_count": sum(native.is_personal_record(r) for r in ordered),
              "material_record_count": sum(not native.is_personal_record(r) for r in ordered),
              "offset": offset, "returned": 0, "records": [], "truncated": offset < len(ordered), "next_cursor": None,
              "max_bytes": max_bytes, "byte_encoding": "utf-8/canonical-json"}
    result["coverage"].update(matched_formal_count=len(all_ids), matched_formal_ids_sha256=native.digest(sorted(all_ids)))
    def set_page():
        result["returned"] = len(result["records"])
        next_offset = offset + result["returned"]
        result["truncated"] = next_offset < len(ordered)
        result["next_cursor"] = base64.urlsafe_b64encode(native.canonical(
            {"version": manifest["version"], "query": query_hash, "offset": next_offset}).encode()).decode() if result["truncated"] and result["returned"] else None
    for record in ordered[offset:]:
        result["records"].append(record)
        set_page()
        candidate = native._bound(dict(result), max_bytes)
        if candidate.get("status") == "budget_too_small":
            result["records"].pop()
            if not result["records"]:
                result["required_min_bytes"] = candidate["required_min_bytes"]
            break
    set_page()
    if result["truncated"] and not result["returned"]:
        result["status"] = "budget_too_small"
    return native._bound(result, max_bytes)
