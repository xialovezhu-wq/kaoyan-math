#!/usr/bin/env python3
"""Thin Study Intake V2 adapter for the canonical Math nightly Skill.

The adapter validates an already frozen outer Capture set and wraps the
native receipt.  It never scans for more captures and never interprets or
writes math card fields.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Mapping


SCHEMA = "study-intake-subject-sol-adapter-invocation-v1"
RESULT_SCHEMA = "study-intake-nightly-sol-adapter-result-v1"
BATCH_SCHEMA = "study-intake-nightly-sol-batch-v2"
AUTHORIZATION_SCHEMA = "study-intake-nightly-command-authorization-v1"
NATIVE_TERMINAL_SCHEMA = "math-nightly-native-terminal-v1"
SUBJECT = "math"
ADAPTER_NAME = "MathNightlySolAdapter"
SKILL_NAME = "kaoyan-math-nightly-qa"
REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = REPO_ROOT / "codex-skill-sources" / SKILL_NAME / "SKILL.md"
NATIVE_ENTRYPOINTS = (
    "数学一回滚复习系统/scripts/quick_intake.py",
    "错题知识网络/scripts/wrongnet.py",
    "数学一回滚复习系统/scripts/scheduler.py",
    "codex-skill-sources/kaoyan-math-nightly-qa/scripts/wiki_parity.py",
)
HARD_CONFLICT_KINDS = {
    "ambiguous_formal_target",
    "immutable_source_conflict",
    "material_formal_choice",
}
ABSOLUTE_COMMAND = re.compile(r"^开始 (\d{4}-\d{2}-\d{2}) 数学正式入库$")
AUTHORIZATION_ID = re.compile(r"^NAUTH-[A-F0-9]{24}$")
BATCH_ID = re.compile(r"^NIGHTLY-[A-F0-9]{28}$")
CONFLICT_ID = re.compile(r"^CONFLICT-[A-F0-9]{24}$")
NATIVE_STATUSES = {"complete", "noop", "awaiting_user", "failed"}
SAFE_NATIVE_STATUSES = {"complete", "noop"}
EXECUTION_EVIDENCE_FIELDS = {
    "pre_state_sha256",
    "post_state_sha256",
    "operations",
    "adapter_run_id",
    "pid",
    "transaction_id",
    "ended_at",
    "stopped_at",
    "exit_code",
}


class AdapterError(ValueError):
    pass


class _FrozenList(list):
    """JSON-compatible recursive immutable list for the native handoff."""

    def _readonly(self, *_args: Any, **_kwargs: Any) -> None:
        raise TypeError("native invocation is immutable")

    __setitem__ = __delitem__ = append = extend = insert = pop = remove = clear = sort = reverse = _readonly
    __iadd__ = __imul__ = _readonly


class _FrozenDict(dict):
    """JSON-compatible recursive immutable mapping for the native handoff."""

    def _readonly(self, *_args: Any, **_kwargs: Any) -> None:
        raise TypeError("native invocation is immutable")

    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = _readonly
    __ior__ = _readonly


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return _FrozenDict({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return _FrozenList(_freeze(item) for item in value)
    if isinstance(value, tuple):
        return _FrozenList(_freeze(item) for item in value)
    return value


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def sha256_value(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _date(value: Any) -> str:
    if not isinstance(value, str):
        raise AdapterError("capture_intake_date_invalid")
    text = value
    try:
        if dt.date.fromisoformat(text).isoformat() != text:
            raise ValueError
    except ValueError as exc:
        raise AdapterError("capture_intake_date_invalid") from exc
    return text


def _sha(value: Any, code: str) -> str:
    text = value
    if not isinstance(text, str) or len(text) != 64 or any(
        char not in "0123456789abcdef" for char in text
    ):
        raise AdapterError(code)
    return text


def _nonempty_text(value: Any, code: str) -> str:
    if not isinstance(value, str) or not value:
        raise AdapterError(code)
    return value


def _command_sha256(command: str) -> str:
    return hashlib.sha256(command.encode("utf-8")).hexdigest()


def _validate_authorization(value: Any, capture_intake_date: str) -> dict[str, str]:
    required = {
        "schema_version",
        "subject",
        "capture_intake_date",
        "normalized_command",
        "command_sha256",
        "authorization_id",
    }
    if not isinstance(value, Mapping) or set(value) != required:
        raise AdapterError("nightly_authorization_shape_invalid")
    if value.get("schema_version") != AUTHORIZATION_SCHEMA:
        raise AdapterError("nightly_authorization_schema_invalid")
    if value.get("subject") != SUBJECT:
        raise AdapterError("nightly_authorization_subject_invalid")
    if value.get("capture_intake_date") != capture_intake_date:
        raise AdapterError("nightly_authorization_date_invalid")
    normalized_command = value.get("normalized_command")
    if not isinstance(normalized_command, str) or normalized_command != normalized_command.strip():
        raise AdapterError("nightly_authorization_command_invalid")
    match = ABSOLUTE_COMMAND.fullmatch(normalized_command)
    if match is None or match.group(1) != capture_intake_date:
        raise AdapterError("nightly_authorization_command_invalid")
    _date(match.group(1))
    command_sha = _sha(
        value.get("command_sha256"), "nightly_authorization_command_sha256_invalid"
    )
    if command_sha != _command_sha256(normalized_command):
        raise AdapterError("nightly_authorization_command_sha256_invalid")
    authorization_id = _nonempty_text(
        value.get("authorization_id"), "nightly_authorization_id_invalid"
    )
    if AUTHORIZATION_ID.fullmatch(authorization_id) is None:
        raise AdapterError("nightly_authorization_id_invalid")
    core = {
        "schema_version": AUTHORIZATION_SCHEMA,
        "subject": SUBJECT,
        "capture_intake_date": capture_intake_date,
        "normalized_command": normalized_command,
        "command_sha256": command_sha,
    }
    if authorization_id != "NAUTH-" + sha256_value(core)[:24].upper():
        raise AdapterError("nightly_authorization_id_invalid")
    return {**core, "authorization_id": authorization_id}


def validate_batch(value: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "schema_version", "batch_id", "subject", "capture_intake_date",
        "capture_ids", "capture_set_sha256", "analysis_packages", "skill",
        "status", "formal_write_count", "authorization",
    }
    if not isinstance(value, Mapping) or set(value) != required:
        raise AdapterError("nightly_batch_shape_invalid")
    if value.get("schema_version") != BATCH_SCHEMA or value.get("subject") != SUBJECT:
        raise AdapterError("nightly_batch_subject_invalid")
    capture_intake_date = _date(value.get("capture_intake_date"))
    if (
        value.get("status") != "frozen"
        or isinstance(value.get("formal_write_count"), bool)
        or value.get("formal_write_count") != 0
    ):
        raise AdapterError("nightly_batch_state_invalid")
    batch_id = _nonempty_text(value.get("batch_id"), "nightly_batch_id_invalid")
    if BATCH_ID.fullmatch(batch_id) is None:
        raise AdapterError("nightly_batch_id_invalid")
    capture_ids = value.get("capture_ids")
    if (
        not isinstance(capture_ids, list)
        or not capture_ids
        or any(not isinstance(item, str) or not item for item in capture_ids)
        or len(capture_ids) != len(set(capture_ids))
        or capture_ids != sorted(capture_ids)
    ):
        raise AdapterError("nightly_batch_capture_ids_invalid")
    expected_set_sha = sha256_value(capture_ids)
    if _sha(value.get("capture_set_sha256"), "capture_set_sha256_invalid") != expected_set_sha:
        raise AdapterError("capture_set_sha256_invalid")
    packages = value.get("analysis_packages")
    if not isinstance(packages, list) or len(packages) != len(capture_ids):
        raise AdapterError("analysis_package_set_invalid")
    package_ids: list[str] = []
    for row in packages:
        if not isinstance(row, Mapping) or set(row) != {
            "capture_id", "package_ref", "package_sha256"
        }:
            raise AdapterError("analysis_package_set_invalid")
        package_id = row.get("capture_id")
        package_sha = _sha(
            row.get("package_sha256"), "analysis_package_sha256_invalid"
        )
        package_ref = row.get("package_ref")
        if (
            not isinstance(package_id, str)
            or not package_id
            or not isinstance(package_ref, str)
            or package_ref
            != "study-intake-analysis-package://sha256/" + package_sha
        ):
            raise AdapterError("analysis_package_ref_invalid")
        package_ids.append(package_id)
    if package_ids != capture_ids:
        raise AdapterError("analysis_package_set_invalid")
    skill = value.get("skill")
    if not isinstance(skill, Mapping) or set(skill) != {
        "name", "source_sha256", "declared_version"
    }:
        raise AdapterError("skill_binding_invalid")
    expected_skill_sha = sha256_file(SKILL_PATH)
    skill_sha = _sha(skill.get("source_sha256"), "skill_source_sha256_invalid")
    if skill.get("name") != SKILL_NAME or skill_sha != expected_skill_sha:
        raise AdapterError("skill_binding_invalid")
    result = copy.deepcopy(dict(value))
    result["capture_intake_date"] = capture_intake_date
    result["authorization"] = _validate_authorization(
        value.get("authorization"), capture_intake_date
    )
    return result


def _validate_selected_ids(
    checked: Mapping[str, Any],
    capture_ids: Any,
    resolution: Any,
) -> tuple[list[str], dict[str, Any] | None]:
    frozen_ids = checked["capture_ids"]
    if resolution is None:
        if capture_ids is None:
            return list(frozen_ids), None
        if not isinstance(capture_ids, list) or capture_ids != frozen_ids:
            raise AdapterError("nightly_selection_must_cover_frozen_batch")
        return list(capture_ids), None

    required = {
        "conflict_id",
        "batch_id",
        "subject",
        "conflicted_capture_id",
        "user_option",
        "skill_name",
        "skill_source_sha256",
    }
    if not isinstance(resolution, Mapping) or set(resolution) != required:
        raise AdapterError("nightly_resolution_shape_invalid")
    if resolution.get("batch_id") != checked["batch_id"]:
        raise AdapterError("nightly_resolution_batch_binding_invalid")
    if resolution.get("subject") != SUBJECT:
        raise AdapterError("nightly_resolution_subject_binding_invalid")
    conflict_id = resolution.get("conflict_id")
    if (
        not isinstance(conflict_id, str)
        or CONFLICT_ID.fullmatch(conflict_id) is None
    ):
        raise AdapterError("nightly_resolution_conflict_id_invalid")
    conflicted_capture_id = resolution.get("conflicted_capture_id")
    if conflicted_capture_id not in frozen_ids:
        raise AdapterError("nightly_resolution_capture_binding_invalid")
    if not isinstance(resolution.get("user_option"), str) or not resolution["user_option"]:
        raise AdapterError("nightly_resolution_user_option_invalid")
    skill = checked["skill"]
    if (
        resolution.get("skill_name") != skill["name"]
        or resolution.get("skill_source_sha256") != skill["source_sha256"]
    ):
        raise AdapterError("nightly_resolution_skill_binding_invalid")
    if capture_ids is None:
        return [conflicted_capture_id], dict(resolution)
    if not isinstance(capture_ids, list) or capture_ids != [conflicted_capture_id]:
        raise AdapterError("nightly_resolution_selection_invalid")
    return [conflicted_capture_id], dict(resolution)


def prepare_invocation(
    batch: Mapping[str, Any],
    *,
    capture_ids: list[str] | None = None,
    resolution: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    checked = validate_batch(batch)
    selected_ids, checked_resolution = _validate_selected_ids(
        checked, capture_ids, resolution
    )
    for relative in NATIVE_ENTRYPOINTS:
        if not (REPO_ROOT / relative).is_file():
            raise AdapterError("native_entrypoint_missing")
    full_run = checked_resolution is None
    core = {
        "schema_version": SCHEMA,
        "adapter_name": ADAPTER_NAME,
        "subject": SUBJECT,
        "batch_id": checked["batch_id"],
        "capture_intake_date": checked["capture_intake_date"],
        "capture_ids": selected_ids,
        "capture_set_sha256": checked["capture_set_sha256"],
        "selected_capture_ids": selected_ids,
        "selected_capture_set_sha256": sha256_value(selected_ids),
        "analysis_packages": [
            package
            for package in checked["analysis_packages"]
            if package["capture_id"] in selected_ids
        ],
        "batch_capture_ids": checked["capture_ids"],
        "batch_capture_set_sha256": checked["capture_set_sha256"],
        "batch_analysis_packages": checked["analysis_packages"],
        "skill": checked["skill"],
        "authorization": checked["authorization"],
        "native_entrypoints": list(NATIVE_ENTRYPOINTS),
        "selection_policy": (
            "outer_frozen_set_only" if full_run else "conflicted_capture_only"
        ),
        "execution_mode": "full_batch" if full_run else "conflict_recovery",
        "resolution": checked_resolution,
        "formal_write_count": 0,
    }
    return _freeze({**core, "invocation_sha256": sha256_value(core)})


def _validate_timezone_timestamp(value: Any, code: str) -> str:
    if not isinstance(value, str) or not value:
        raise AdapterError(code)
    text = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError as exc:
        raise AdapterError(code) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise AdapterError(code)
    return value


def _validate_execution_evidence(value: Any, status: str) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != EXECUTION_EVIDENCE_FIELDS:
        raise AdapterError("execution_evidence_shape_invalid")
    _sha(value.get("pre_state_sha256"), "execution_pre_state_sha256_invalid")
    _sha(value.get("post_state_sha256"), "execution_post_state_sha256_invalid")
    if not isinstance(value.get("operations"), list):
        raise AdapterError("execution_operations_invalid")
    try:
        canonical_bytes(value["operations"])
    except (TypeError, ValueError) as exc:
        raise AdapterError("execution_operations_invalid") from exc
    _nonempty_text(value.get("adapter_run_id"), "execution_adapter_run_id_invalid")
    pid = value.get("pid")
    if isinstance(pid, bool) or not isinstance(pid, int) or pid <= 0:
        raise AdapterError("execution_pid_invalid")
    _nonempty_text(value.get("transaction_id"), "execution_transaction_id_invalid")
    ended_at = _validate_timezone_timestamp(
        value.get("ended_at"), "execution_ended_at_invalid"
    )
    stopped_at = _validate_timezone_timestamp(
        value.get("stopped_at"), "execution_stopped_at_invalid"
    )
    ended_text = ended_at[:-1] + "+00:00" if ended_at.endswith("Z") else ended_at
    stopped_text = (
        stopped_at[:-1] + "+00:00" if stopped_at.endswith("Z") else stopped_at
    )
    if dt.datetime.fromisoformat(ended_text) > dt.datetime.fromisoformat(stopped_text):
        raise AdapterError("execution_timeline_invalid")
    exit_code = value.get("exit_code")
    if isinstance(exit_code, bool) or not isinstance(exit_code, int):
        raise AdapterError("execution_exit_code_invalid")
    if status in {"complete", "noop", "awaiting_user"} and exit_code != 0:
        raise AdapterError("execution_success_exit_code_invalid")
    if status == "failed" and exit_code == 0:
        raise AdapterError("execution_failure_exit_code_invalid")
    return dict(value)


def _conflict_id(checked: Mapping[str, Any], conflict: Mapping[str, Any]) -> str:
    skill = checked["skill"]
    return "CONFLICT-" + sha256_value(
        {
            "subject": SUBJECT,
            "batch_id": checked["batch_id"],
            "capture_id": conflict["capture_id"],
            "kind": conflict["kind"],
            "skill_name": skill["name"],
            "skill_source_sha256": skill["source_sha256"],
        }
    )[:24].upper()


def _validate_close_receipt(
    native_receipt: Mapping[str, Any], selected_ids: list[str]
) -> None:
    close_receipt = native_receipt.get("quick_intake_close_receipt")
    close_sha = native_receipt.get("quick_intake_close_receipt_sha256")
    status = native_receipt.get("status")
    if status in SAFE_NATIVE_STATUSES:
        required = {
            "status", "state", "closeout_id", "freeze_id", "study_date",
            "artifact_date", "closed_event_ids", "content_hash", "elapsed_ms",
            "receipt_file_consumed",
        }
        if not isinstance(close_receipt, Mapping) or set(close_receipt) != required:
            raise AdapterError("quick_intake_close_receipt_invalid")
        expected_close_status = "recorded" if status == "complete" else "noop"
        if close_receipt.get("status") != expected_close_status:
            raise AdapterError("quick_intake_close_receipt_status_invalid")
        if close_receipt.get("state") != "nightly_closed":
            raise AdapterError("quick_intake_close_receipt_state_invalid")
        freeze_id = native_receipt.get("freeze_id")
        if (
            not isinstance(freeze_id, str)
            or re.fullmatch(r"MFI-FREEZE-[0-9a-f]{24}", freeze_id) is None
            or close_receipt.get("freeze_id") != freeze_id
        ):
            raise AdapterError("quick_intake_close_receipt_freeze_binding_invalid")
        if (
            not isinstance(close_receipt.get("closeout_id"), str)
            or re.fullmatch(
                r"MFI-CLOSE-[0-9a-f]{24}", close_receipt["closeout_id"]
            )
            is None
        ):
            raise AdapterError("quick_intake_close_receipt_closeout_id_invalid")
        _date(close_receipt.get("study_date"))
        _date(close_receipt.get("artifact_date"))
        closed_ids = close_receipt.get("closed_event_ids")
        if (
            not isinstance(closed_ids, list)
            or any(not isinstance(item, str) or not item for item in closed_ids)
            or len(closed_ids) != len(set(closed_ids))
            or set(closed_ids) != set(selected_ids)
        ):
            raise AdapterError("quick_intake_close_receipt_events_invalid")
        _sha(close_receipt.get("content_hash"), "quick_intake_content_hash_invalid")
        elapsed = close_receipt.get("elapsed_ms")
        if (
            isinstance(elapsed, bool)
            or not isinstance(elapsed, (int, float))
            or elapsed < 0
            or not isinstance(close_receipt.get("receipt_file_consumed"), bool)
        ):
            raise AdapterError("quick_intake_close_receipt_runtime_invalid")
        try:
            expected_close_sha = sha256_value(close_receipt)
        except (TypeError, ValueError) as exc:
            raise AdapterError("quick_intake_close_receipt_invalid") from exc
        if _sha(close_sha, "quick_intake_close_receipt_sha256_invalid") != expected_close_sha:
            raise AdapterError("quick_intake_close_receipt_sha256_invalid")
        return
    if close_receipt is not None or close_sha is not None:
        raise AdapterError("quick_intake_close_receipt_unexpected")


def _validate_native_terminal(
    checked: Mapping[str, Any],
    native_receipt: Mapping[str, Any],
    selected_ids: list[str],
) -> tuple[dict[str, Any], str | None]:
    required = {
        "schema_version",
        "subject",
        "batch_id",
        "freeze_id",
        "status",
        "capture_results",
        "changed_files",
        "formal_write_count",
        "conflict",
        "quick_intake_close_receipt",
        "quick_intake_close_receipt_sha256",
        "execution_evidence",
    }
    if not isinstance(native_receipt, Mapping) or set(native_receipt) != required:
        raise AdapterError("native_receipt_shape_invalid")
    try:
        canonical_bytes(native_receipt)
    except (TypeError, ValueError) as exc:
        raise AdapterError("native_receipt_json_invalid") from exc
    if native_receipt.get("schema_version") != NATIVE_TERMINAL_SCHEMA:
        raise AdapterError("native_receipt_schema_invalid")
    if (
        native_receipt.get("subject") != SUBJECT
        or native_receipt.get("batch_id") != checked["batch_id"]
    ):
        raise AdapterError("native_receipt_binding_invalid")
    freeze_id = _nonempty_text(native_receipt.get("freeze_id"), "native_freeze_id_invalid")
    status = native_receipt.get("status")
    if status not in NATIVE_STATUSES:
        raise AdapterError("native_receipt_status_invalid")
    formal_write_count = native_receipt.get("formal_write_count")
    if (
        isinstance(formal_write_count, bool)
        or not isinstance(formal_write_count, int)
        or formal_write_count < 0
    ):
        raise AdapterError("native_receipt_formal_write_count_invalid")
    changed_files = native_receipt.get("changed_files")
    if (
        not isinstance(changed_files, list)
        or any(not isinstance(item, str) or not item for item in changed_files)
        or len(changed_files) != len(set(changed_files))
    ):
        raise AdapterError("native_changed_files_invalid")
    capture_results = native_receipt.get("capture_results")
    if not isinstance(capture_results, list):
        raise AdapterError("native_capture_results_invalid")
    result_ids: list[str] = []
    for row in capture_results:
        if not isinstance(row, Mapping):
            raise AdapterError("native_capture_results_invalid")
        capture_id = row.get("capture_id")
        if capture_id not in selected_ids or capture_id in result_ids:
            raise AdapterError("native_capture_results_invalid")
        result_ids.append(capture_id)
    if result_ids != sorted(result_ids):
        raise AdapterError("native_capture_results_invalid")
    conflict = native_receipt.get("conflict")
    conflict_id: str | None = None
    if status == "awaiting_user":
        if (
            not isinstance(conflict, Mapping)
            or conflict.get("kind") not in HARD_CONFLICT_KINDS
            or conflict.get("capture_id") not in selected_ids
        ):
            raise AdapterError("hard_conflict_invalid")
        conflicted_id = conflict["capture_id"]
        if set(result_ids) != set(selected_ids) - {conflicted_id}:
            raise AdapterError("native_capture_results_conflict_invalid")
        conflict_id = _conflict_id(checked, conflict)
        supplied_conflict_id = conflict.get("conflict_id")
        if supplied_conflict_id is not None and supplied_conflict_id != conflict_id:
            raise AdapterError("hard_conflict_id_invalid")
    else:
        if conflict is not None or set(result_ids) != set(selected_ids):
            raise AdapterError("native_capture_results_invalid")
    if status == "failed" and formal_write_count != 0:
        raise AdapterError("native_failed_formal_write_count_nonzero")
    _validate_execution_evidence(native_receipt.get("execution_evidence"), status)
    _validate_close_receipt(native_receipt, selected_ids)
    receipt = copy.deepcopy(dict(native_receipt))
    receipt["freeze_id"] = freeze_id
    return receipt, conflict_id


def validate_native_terminal(
    batch: Mapping[str, Any],
    native_receipt: Mapping[str, Any],
    *,
    capture_ids: list[str] | None = None,
    selected_capture_ids: list[str] | None = None,
    resolution: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Strictly validate and return the opaque native terminal envelope."""
    checked = validate_batch(batch)
    if capture_ids is not None and selected_capture_ids is not None:
        if capture_ids != selected_capture_ids:
            raise AdapterError("native_capture_scope_conflict")
    if capture_ids is None:
        capture_ids = selected_capture_ids
    selected_ids, _ = _validate_selected_ids(checked, capture_ids, resolution)
    receipt, _ = _validate_native_terminal(checked, native_receipt, selected_ids)
    return receipt


def wrap_native_receipt(
    batch: Mapping[str, Any],
    native_receipt: Mapping[str, Any],
    *,
    capture_ids: list[str] | None = None,
    selected_capture_ids: list[str] | None = None,
    resolution: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    checked = validate_batch(batch)
    if capture_ids is not None and selected_capture_ids is not None:
        if capture_ids != selected_capture_ids:
            raise AdapterError("native_capture_scope_conflict")
    if capture_ids is None:
        capture_ids = selected_capture_ids
    selected_ids, _ = _validate_selected_ids(checked, capture_ids, resolution)
    receipt, conflict_id = _validate_native_terminal(checked, native_receipt, selected_ids)
    status_map = {
        "complete": "complete",
        "noop": "noop",
        "awaiting_user": "awaiting_user",
        "failed": "failed",
    }
    return {
        "schema_version": RESULT_SCHEMA,
        "adapter_name": ADAPTER_NAME,
        "subject": SUBJECT,
        "batch_id": checked["batch_id"],
        "status": status_map[receipt["status"]],
        "native_receipt": receipt,
        "native_receipt_sha256": sha256_value(receipt),
        "conflict_id": conflict_id,
        "formal_write_count": int(receipt["formal_write_count"]),
    }


class MathNightlySolAdapter:
    """Callable Math boundary for one frozen nightly batch or one recovery item."""

    def execute(
        self,
        batch: Mapping[str, Any],
        *,
        native_executor: Any,
        capture_ids: list[str] | None = None,
        resolution: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        if not callable(native_executor):
            raise AdapterError("native_executor_invalid")
        checked = validate_batch(batch)
        selected_ids, _ = _validate_selected_ids(checked, capture_ids, resolution)
        if resolution is None and selected_ids == checked["capture_ids"] and capture_ids is None:
            invocation = prepare_invocation(checked)
        else:
            invocation = prepare_invocation(
                checked, capture_ids=selected_ids, resolution=resolution
            )
        native_receipt = native_executor(invocation)
        return wrap_native_receipt(
            checked,
            native_receipt,
            capture_ids=selected_ids,
            resolution=resolution,
        )


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AdapterError("json_object_required")
    return value


def _write(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "wb") as handle:
            handle.write(canonical_bytes(value)); handle.flush(); os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        try:
            Path(name).unlink()
        except FileNotFoundError:
            pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "wrap"):
        command = sub.add_parser(name)
        command.add_argument("--batch", type=Path, required=True)
        command.add_argument("--output", type=Path, required=True)
        if name == "wrap":
            command.add_argument("--native-receipt", type=Path, required=True)
    args = parser.parse_args(argv)
    batch = _load(args.batch)
    result = (
        prepare_invocation(batch)
        if args.command == "prepare"
        else wrap_native_receipt(batch, _load(args.native_receipt))
    )
    _write(args.output, result)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
