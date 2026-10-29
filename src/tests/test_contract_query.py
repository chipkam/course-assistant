"""Contract: a golden frame against the golden KB gives the golden result (§5).

Both the frame and the KB come from golden files, so this stage is tested
without the semantic stage or the KB loader.  ``query`` and ``reason`` are free
text; ``found``, ``kind``, ``sources`` and, when found, ``data`` are fixed.
"""

import unittest

from hcmut.iaslab.nlp.app.kb import KnowledgeBase
from hcmut.iaslab.nlp.app.query import QueryEngine

from tests.contract_support import ContractTestCase, frame, load, load_json, plain, short


def golden_kb() -> KnowledgeBase:
    data = load_json("kb.json")
    data["resources"] = tuple(data["resources"])
    return KnowledgeBase(**data)


class QueryContractTests(ContractTestCase):
    def test_results_match_golden(self) -> None:
        engine = QueryEngine(golden_kb())

        def check(record):
            actual = engine.execute(frame(record["frame"]))
            expected = record["result"]
            problems = []
            for name in ("found", "kind"):
                if getattr(actual, name) != expected[name]:
                    problems.append(f"{name}: expected {expected[name]!r} got {getattr(actual, name)!r}")
            if list(actual.sources) != expected["sources"]:
                problems.append(f"sources: expected {expected['sources']} got {list(actual.sources)}")
            if expected["found"] and plain(actual.data) != expected["data"]:
                problems.append(f"data: expected {short(expected['data'])} got {short(plain(actual.data))}")
            if problems:
                return f"{short(record['frame'], 100)}:\n    " + "\n    ".join(problems)
            return None

        self.check_all(load("query.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
