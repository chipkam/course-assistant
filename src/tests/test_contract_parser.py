"""Contract: the parser builds the golden tree, or none for rejected text (§2)."""

import unittest

from hcmut.iaslab.nlp.app.grammar import Grammar
from hcmut.iaslab.nlp.app.parser import EarleyParser

from tests.contract_support import DATA, ContractTestCase, load, short, tree


class ParserContractTests(ContractTestCase):
    def test_grammar_has_the_26_question_branches(self) -> None:
        grammar = self.build(lambda: Grammar.from_file(DATA / "grammar.cfg"))
        branches = [rule.rhs[0] for rule in grammar.rules_for("QUESTION") if len(rule.rhs) == 1]
        self.assertEqual(len(branches), 26)
        self.assertTrue(all(name.startswith("Q_") for name in branches))

    def test_trees_match_golden(self) -> None:
        parser = self.build(lambda: EarleyParser(Grammar.from_file(DATA / "grammar.cfg")))

        def check(record):
            parsed = parser.parse(record["sentence"])
            expected = tree(record["tree"])
            if parsed.tree != expected:
                got = parsed.tree.bracketed() if parsed.tree else "()"
                want = expected.bracketed() if expected else "()"
                return f"{record['sentence']!r}:\n    expected {short(want)}\n    got      {short(got)}"
            return None

        self.check_all(load("parser.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
