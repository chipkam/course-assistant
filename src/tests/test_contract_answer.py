"""Contract: the answer has the right category and required facts (§6).

Wording is free.  Fixed: which fallback message is used, that a found result is
never answered with a fallback, and that every required fact appears.
"""

import unittest

from hcmut.iaslab.nlp.app.answer import MISSING_CONTEXT, NOT_FOUND, NOT_UNDERSTOOD, AnswerGenerator

from tests.contract_support import ContractTestCase, frame, load, normalize, result, short

FALLBACKS = {NOT_FOUND: "NOT_FOUND", NOT_UNDERSTOOD: "NOT_UNDERSTOOD", MISSING_CONTEXT: "MISSING_CONTEXT"}


class AnswerContractTests(ContractTestCase):
    def test_answers_match_golden(self) -> None:
        generator = AnswerGenerator()

        def check(record):
            text = generator.generate(frame(record["frame"]), result(record["result"]))
            category = FALLBACKS.get(text, "FOUND")
            if category != record["category"]:
                return f"{short(record['frame'], 100)}: expected {record['category']} got {category}: {short(text)}"
            missing = [term for term in record["must_contain"] if normalize(term) not in normalize(text)]
            if missing:
                return f"{short(record['frame'], 100)}: missing facts {missing} in {short(text)}"
            if category == "FOUND" and not text.strip():
                return f"{short(record['frame'], 100)}: empty answer"
            return None

        self.check_all(load("answer.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
