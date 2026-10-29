"""Contract: tokenize() returns exactly the grammar terminals (docs/contracts.md §1)."""

import unittest

from hcmut.iaslab.nlp.app.tokenizer import tokenize

from tests.contract_support import ContractTestCase, load, short


class TokenizerContractTests(ContractTestCase):
    def test_tokens_match_golden(self) -> None:
        def check(record):
            actual = tokenize(record["text"])
            if list(actual) != record["tokens"]:
                return f"{record['text']!r}: expected {record['tokens']} got {short(list(actual))}"
            return None

        self.check_all(load("tokenizer.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
