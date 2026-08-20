"""Small deterministic wrong-card parser for hermetic quick-intake tests."""

from __future__ import annotations

from pathlib import Path


BASE_DIR = Path(".")
CARDS_DIR = Path(".")
OUT_DIR = Path(".")


def _frontmatter(text: str) -> dict[str, object]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    result: dict[str, object] = {}
    active_list: str | None = None
    for raw in lines[1:end]:
        if raw.startswith("  - ") and active_list is not None:
            value = raw[4:].strip().strip('"')
            current = result.setdefault(active_list, [])
            if isinstance(current, list):
                current.append(value)
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


def read_cards() -> list[dict[str, object]]:
    cards: list[dict[str, object]] = []
    for card_path in sorted(CARDS_DIR.glob("*.md")):
        meta = _frontmatter(card_path.read_text(encoding="utf-8"))
        card_id = meta.get("id")
        if not isinstance(card_id, str) or not card_id:
            continue
        cards.append(
            {
                "id": card_id,
                "relpath": card_path.relative_to(BASE_DIR).as_posix(),
                "meta": meta,
                "topic_chains": [],
            }
        )
    return cards
