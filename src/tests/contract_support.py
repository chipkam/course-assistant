"""Shared helpers for the stage-contract tests described in docs/contracts.md.

Golden records in ``tests/golden/`` are produced by ``tools/make_golden.py`` from
the frozen reference implementation.  Each contract test feeds one stage the
golden input of that stage and compares only the fields the contract fixes, so
stages can be built and accepted independently.  A stage that still raises
``NotImplementedError`` is skipped, so "not started" stays distinct from "wrong".
"""

from __future__ import annotations

import json
import unicodedata
import unittest
from pathlib import Path
from typing import Any, Callable, Iterable

from hcmut.iaslab.nlp.app.query import QueryResult
from hcmut.iaslab.nlp.app.semantic import SemanticFrame
from hcmut.iaslab.nlp.app.tree import Tree

GOLDEN = Path(__file__).with_name("golden")
SRC = Path(__file__).resolve().parents[1]
DATA = SRC / "data"
MAX_REPORTED = 10


def load(name: str) -> list[dict[str, Any]]:
    with (GOLDEN / name).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_json(name: str) -> Any:
    return json.loads((GOLDEN / name).read_text(encoding="utf-8"))


def plain(value: Any) -> Any:
    """JSON-normalize so tuples and lists, or nested records, compare equal."""
    return json.loads(json.dumps(value, ensure_ascii=False, default=list))


def tree(value: Any) -> Tree | None:
    """Rebuild a golden ``[label, child, ...]`` list into a ``Tree``."""
    if value is None:
        return None
    label, *children = value
    return Tree(label, tuple(tree(c) if isinstance(c, list) else c for c in children))


def frame(value: dict[str, Any]) -> SemanticFrame:
    return SemanticFrame(value["intent"], value["entity"], dict(value["slots"]), value["source_branch"])


def frame_dict(value: SemanticFrame) -> dict[str, Any]:
    return {
        "intent": value.intent,
        "entity": value.entity,
        "slots": plain(value.slots),
        "source_branch": value.source_branch,
    }


def result(value: dict[str, Any]) -> QueryResult:
    return QueryResult(
        value["query"], value["found"], value["kind"], value["data"],
        list(value["sources"]), value.get("reason"),
    )


def normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).lower().split())


def short(value: Any, limit: int = 160) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return text if len(text) <= limit else text[: limit - 1] + "…"


class ContractTestCase(unittest.TestCase):
    """Run one check per golden record and report mismatches together."""

    def check_all(self, records: Iterable[Any], check: Callable[[Any], str | None]) -> None:
        records = list(records)
        failures: list[str] = []
        for record in records:
            try:
                message = check(record)
            except NotImplementedError as exc:
                self.skipTest(f"stage chưa hiện thực: {exc}")
            except Exception as exc:  # one bad record must not hide the others
                message = f"{type(exc).__name__}: {exc}"
            if message:
                failures.append(message)
        if failures:
            shown = "\n- ".join(failures[:MAX_REPORTED])
            more = f"\n… và {len(failures) - MAX_REPORTED} bản ghi khác" if len(failures) > MAX_REPORTED else ""
            self.fail(f"{len(failures)}/{len(records)} bản ghi sai hợp đồng:\n- {shown}{more}")

    def build(self, factory: Callable[[], Any]) -> Any:
        """Construct a stage, skipping the test while it is not implemented."""
        try:
            return factory()
        except NotImplementedError as exc:
            self.skipTest(f"stage chưa hiện thực: {exc}")
