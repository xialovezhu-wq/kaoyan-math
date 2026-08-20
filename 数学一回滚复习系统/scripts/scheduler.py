"""Portable semantic source-version helpers used by quick-intake closeout.

The complete personal review scheduler is deliberately outside this canonical
source repository.  These pure helpers preserve the content-addressed source
version contract without reading queues, scores, or user runtime data.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def _canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def parse_card_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    result: dict[str, Any] = {}
    active_list: str | None = None
    for raw in lines[1:end]:
        if raw.startswith("  - ") and active_list is not None:
            current = result.setdefault(active_list, [])
            if isinstance(current, list):
                current.append(raw[4:].strip().strip('"'))
            continue
        active_list = None
        if ":" not in raw or raw.startswith(" "):
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            result[key] = value.strip('"')
        else:
            result[key] = []
            active_list = key
    return result


def extract_explicit_wrong_events(
    formal_id: str, data: dict[str, Any]
) -> list[Any]:
    value = data.get("wrong_events", [])
    return list(value) if isinstance(value, list) else []


def wrongnet_metadata_from_card(
    formal_id: str, data: dict[str, Any]
) -> dict[str, Any]:
    return {
        "formal_id": formal_id,
        "knowledge": data.get("knowledge", []),
        "methods": data.get("methods", []),
        "status": data.get("status"),
        "subject": data.get("subject"),
    }


def method_gap_fingerprint(data: dict[str, Any]) -> str | None:
    method_gap = data.get("method_gap")
    if method_gap in (None, "", [], {}):
        return None
    return hashlib.sha256(_canonical_bytes(method_gap)).hexdigest()


def source_sync_version(
    formal_id: str,
    data: dict[str, Any],
    metadata: dict[str, Any],
    events: list[Any],
    method_fingerprint: str | None,
) -> str:
    semantic = {
        "formal_id": formal_id,
        "frontmatter": data,
        "wrongnet_metadata": metadata,
        "explicit_wrong_events": events,
        "method_gap_fingerprint": method_fingerprint,
    }
    return hashlib.sha256(_canonical_bytes(semantic)).hexdigest()
