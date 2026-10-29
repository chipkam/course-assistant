"""Contract: KnowledgeBase.load builds exactly the golden normalized KB (§4)."""

import unittest

from hcmut.iaslab.nlp.app.kb import KnowledgeBase

from tests.contract_support import DATA, ContractTestCase, load_json, plain, short


class KnowledgeBaseContractTests(ContractTestCase):
    def test_collections_match_golden(self) -> None:
        kb = self.build(lambda: KnowledgeBase.load(DATA / "kb"))
        golden = load_json("kb.json")

        def check(name):
            actual, expected = plain(getattr(kb, name)), golden[name]
            if actual == expected:
                return None
            if isinstance(expected, dict) and isinstance(actual, dict):
                missing = sorted(set(expected) - set(actual))
                extra = sorted(set(actual) - set(expected))
                wrong = sorted(k for k in set(expected) & set(actual) if expected[k] != actual[k])
                first = f"; first wrong {wrong[0]!r}: expected {short(expected[wrong[0]])} got {short(actual[wrong[0]])}" if wrong else ""
                return f"{name}: missing {missing[:5]} extra {extra[:5]} wrong {wrong[:5]}{first}"
            return f"{name}: expected {short(expected)} got {short(actual)}"

        self.check_all(sorted(golden), check)

    def test_supplied_kb_is_valid(self) -> None:
        kb = self.build(lambda: KnowledgeBase.load(DATA / "kb"))
        errors = self.build(kb.validate)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
