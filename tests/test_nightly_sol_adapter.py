from __future__ import annotations

import hashlib
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "数学一回滚复习系统/scripts/nightly_sol_adapter.py"
SPEC = importlib.util.spec_from_file_location("math_nightly_sol_adapter", MODULE_PATH)
assert SPEC and SPEC.loader
adapter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(adapter)


def batch() -> dict:
    captures = ["CAP-MATH-001", "CAP-MATH-002", "CAP-MATH-003"]
    day = "2026-08-21"
    command = f"开始 {day} 数学正式入库"
    skill_sha = adapter.sha256_file(adapter.SKILL_PATH)
    core_authorization = {
        "schema_version": adapter.AUTHORIZATION_SCHEMA,
        "subject": "math",
        "capture_intake_date": day,
        "normalized_command": command,
        "command_sha256": hashlib.sha256(command.encode("utf-8")).hexdigest(),
    }
    return {
        "schema_version": adapter.BATCH_SCHEMA,
        "batch_id": "NIGHTLY-" + "A" * 28,
        "subject": "math",
        "capture_intake_date": day,
        "capture_ids": captures,
        "capture_set_sha256": adapter.sha256_value(captures),
        "analysis_packages": [
            {
                "capture_id": item,
                "package_ref": "study-intake-analysis-package://sha256/" + str(index) * 64,
                "package_sha256": str(index) * 64,
            }
            for index, item in enumerate(captures, start=1)
        ],
        "skill": {
            "name": adapter.SKILL_NAME,
            "source_sha256": skill_sha,
            "declared_version": None,
        },
        "authorization": {
            **core_authorization,
            "authorization_id": "NAUTH-" + adapter.sha256_value(core_authorization)[:24].upper(),
        },
        "status": "frozen",
        "formal_write_count": 0,
    }


def execution_evidence() -> dict:
    return {
        "pre_state_sha256": "1" * 64,
        "post_state_sha256": "2" * 64,
        "operations": [{"opaque": "math fields are not interpreted here"}],
        "adapter_run_id": "RUN-MATH-001",
        "pid": 12345,
        "transaction_id": "TX-MATH-001",
        "ended_at": "2026-08-21T22:00:00+08:00",
        "stopped_at": "2026-08-21T22:00:01+08:00",
        "exit_code": 0,
    }


def close_receipt(freeze_id: str, capture_ids: list[str], *, status: str = "recorded") -> dict:
    return {
        "status": status,
        "state": "nightly_closed",
        "closeout_id": "MFI-CLOSE-" + "1" * 24,
        "freeze_id": freeze_id,
        "study_date": "2026-08-21",
        "artifact_date": "2026-08-21",
        "closed_event_ids": list(capture_ids),
        "content_hash": "3" * 64,
        "elapsed_ms": 1.0,
        "receipt_file_consumed": True,
    }


def terminal(
    source_batch: dict,
    *,
    status: str = "complete",
    selected: list[str] | None = None,
    results: list[dict] | None = None,
    conflict: dict | None = None,
    freeze_id: str = "MFI-FREEZE-" + "0" * 24,
) -> dict:
    selected = list(selected or source_batch["capture_ids"])
    if results is None:
        results = [
            {"capture_id": capture_id, "opaque": {"result": "synthetic"}}
            for capture_id in selected
        ]
    safe = status in {"complete", "committed", "noop"}
    close = (
        close_receipt(
            freeze_id,
            selected,
            status="noop" if status == "noop" else "recorded",
        )
        if safe
        else None
    )
    return {
        "schema_version": adapter.NATIVE_TERMINAL_SCHEMA,
        "subject": "math",
        "batch_id": source_batch["batch_id"],
        "freeze_id": freeze_id,
        "status": status,
        "capture_results": results,
        "changed_files": ["synthetic/math-card.md"] if safe else ["synthetic/a.md"],
        "formal_write_count": len(results),
        "conflict": conflict,
        "quick_intake_close_receipt": close,
        "quick_intake_close_receipt_sha256": (
            adapter.sha256_value(close) if close is not None else None
        ),
        "execution_evidence": execution_evidence(),
    }


class MathNightlySolAdapterTests(unittest.TestCase):
    def test_prepare_binds_outer_set_real_skill_and_immutable_handoff(self) -> None:
        source = batch()
        invocation = adapter.prepare_invocation(source)
        self.assertEqual(invocation["selection_policy"], "outer_frozen_set_only")
        self.assertEqual(invocation["capture_ids"], source["capture_ids"])
        self.assertEqual(invocation["formal_write_count"], 0)
        with self.assertRaises(TypeError):
            invocation["capture_ids"].append("CAP-MATH-004")
        with self.assertRaises(TypeError):
            invocation["skill"]["source_sha256"] = "f" * 64

    def test_skill_hash_or_package_set_drift_fails_closed(self) -> None:
        drifted = batch()
        drifted["skill"]["source_sha256"] = "f" * 64
        with self.assertRaisesRegex(adapter.AdapterError, "skill_binding_invalid"):
            adapter.prepare_invocation(drifted)
        drifted = batch()
        drifted["analysis_packages"].reverse()
        with self.assertRaisesRegex(adapter.AdapterError, "analysis_package_set_invalid"):
            adapter.prepare_invocation(drifted)

    def test_exact_authorization_drift_fails(self) -> None:
        drifted = batch()
        drifted["authorization"]["normalized_command"] = "开始 2026-08-21 数学正式入库 "
        with self.assertRaisesRegex(adapter.AdapterError, "nightly_authorization_command_invalid"):
            adapter.prepare_invocation(drifted)
        drifted = batch()
        drifted["authorization"]["command_sha256"] = "f" * 64
        with self.assertRaisesRegex(
            adapter.AdapterError, "nightly_authorization_command_sha256_invalid"
        ):
            adapter.prepare_invocation(drifted)

    def test_execute_calls_native_executor_once_with_full_immutable_invocation(self) -> None:
        source = batch()
        calls: list[object] = []

        def executor(invocation: object) -> dict:
            calls.append(invocation)
            self.assertEqual(invocation["capture_ids"], source["capture_ids"])
            with self.assertRaises(TypeError):
                invocation["capture_ids"].append("CAP-MATH-004")
            return terminal(source)

        result = adapter.MathNightlySolAdapter().execute(source, native_executor=executor)
        self.assertEqual(len(calls), 1)
        self.assertEqual(result["status"], "complete")
        self.assertEqual(
            result["native_receipt_sha256"],
            adapter.sha256_value(result["native_receipt"]),
        )

    def test_real_close_receipt_is_bound_to_freeze_and_hash(self) -> None:
        source = batch()
        native = terminal(source)
        result = adapter.wrap_native_receipt(source, native)
        self.assertEqual(
            result["native_receipt"]["quick_intake_close_receipt"]["freeze_id"],
            "MFI-FREEZE-" + "0" * 24,
        )

        drifted = terminal(source)
        drifted["quick_intake_close_receipt"]["freeze_id"] = "FREEZE-OTHER"
        with self.assertRaisesRegex(
            adapter.AdapterError, "quick_intake_close_receipt_freeze_binding_invalid"
        ):
            adapter.wrap_native_receipt(source, drifted)

        drifted = terminal(source)
        drifted["quick_intake_close_receipt_sha256"] = "f" * 64
        with self.assertRaisesRegex(
            adapter.AdapterError, "quick_intake_close_receipt_sha256_invalid"
        ):
            adapter.wrap_native_receipt(source, drifted)

    def test_full_batch_can_return_a_c_safe_and_b_hard_conflict(self) -> None:
        source = batch()
        conflict = {
            "kind": "ambiguous_formal_target",
            "capture_id": "CAP-MATH-002",
        }
        native = terminal(
            source,
            status="awaiting_user",
            results=[
                {"capture_id": "CAP-MATH-001", "opaque": {"safe": "A"}},
                {"capture_id": "CAP-MATH-003", "opaque": {"safe": "C"}},
            ],
            conflict=conflict,
        )
        native["formal_write_count"] = 2
        result = adapter.wrap_native_receipt(source, native)
        self.assertEqual(result["status"], "awaiting_user")
        self.assertTrue(result["conflict_id"].startswith("CONFLICT-"))
        self.assertNotIn(
            "CAP-MATH-002",
            [row["capture_id"] for row in result["native_receipt"]["capture_results"]],
        )
        self.assertEqual(
            result["conflict_id"], adapter.wrap_native_receipt(source, native)["conflict_id"]
        )

    def test_resolution_only_calls_conflicted_capture(self) -> None:
        source = batch()
        conflict = {
            "kind": "ambiguous_formal_target",
            "capture_id": "CAP-MATH-002",
        }
        first = adapter.wrap_native_receipt(
            source,
            terminal(
                source,
                status="awaiting_user",
                results=[
                    {"capture_id": "CAP-MATH-001"},
                    {"capture_id": "CAP-MATH-003"},
                ],
                conflict=conflict,
            ),
        )
        resolution = {
            "conflict_id": first["conflict_id"],
            "batch_id": source["batch_id"],
            "subject": "math",
            "conflicted_capture_id": "CAP-MATH-002",
            "user_option": "use-existing-formal-target",
            "skill_name": source["skill"]["name"],
            "skill_source_sha256": source["skill"]["source_sha256"],
        }
        calls: list[object] = []

        def executor(invocation: object) -> dict:
            calls.append(invocation)
            self.assertEqual(invocation["capture_ids"], ["CAP-MATH-002"])
            self.assertEqual(invocation["resolution"], resolution)
            return terminal(source, selected=["CAP-MATH-002"])

        result = adapter.MathNightlySolAdapter().execute(
            source,
            native_executor=executor,
            resolution=resolution,
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(result["status"], "complete")

    def test_receipt_and_hash_drift_fail_closed(self) -> None:
        source = batch()
        drifted = terminal(source)
        drifted["execution_evidence"]["post_state_sha256"] = "not-a-hash"
        with self.assertRaisesRegex(
            adapter.AdapterError, "execution_post_state_sha256_invalid"
        ):
            adapter.wrap_native_receipt(source, drifted)
        drifted = terminal(source)
        drifted["execution_evidence"]["exit_code"] = 1
        with self.assertRaisesRegex(adapter.AdapterError, "execution_success_exit_code_invalid"):
            adapter.wrap_native_receipt(source, drifted)

    def test_only_three_hard_conflicts_create_awaiting_user(self) -> None:
        source = batch()
        for kind in adapter.HARD_CONFLICT_KINDS:
            native = terminal(
                source,
                status="awaiting_user",
                results=[
                    {"capture_id": "CAP-MATH-001"},
                    {"capture_id": "CAP-MATH-003"},
                ],
                conflict={"kind": kind, "capture_id": "CAP-MATH-002"},
            )
            result = adapter.wrap_native_receipt(source, native)
            self.assertEqual(result["status"], "awaiting_user")
        native = terminal(
            source,
            status="awaiting_user",
            results=[
                {"capture_id": "CAP-MATH-001"},
                {"capture_id": "CAP-MATH-003"},
            ],
            conflict={"kind": "ordinary_warning", "capture_id": "CAP-MATH-002"},
        )
        with self.assertRaisesRegex(adapter.AdapterError, "hard_conflict_invalid"):
            adapter.wrap_native_receipt(source, native)


if __name__ == "__main__":
    unittest.main()
