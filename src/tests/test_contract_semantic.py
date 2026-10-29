"""Contract: a golden tree maps to the golden SemanticFrame (§3).

The tree comes from the golden file, so this stage is tested without the parser.
"""

import unittest

from hcmut.iaslab.nlp.app.entities import EntityLexicon
from hcmut.iaslab.nlp.app.semantic import SemanticInterpreter

from tests.contract_support import DATA, ContractTestCase, frame_dict, load, short, tree


class SemanticContractTests(ContractTestCase):
    def test_frames_match_golden(self) -> None:
        lexicon = self.build(lambda: EntityLexicon.from_file(DATA / "scaffolding" / "entities.txt"))
        interpreter = SemanticInterpreter(lexicon)

        def check(record):
            actual = frame_dict(interpreter.interpret(tree(record["tree"])))
            if actual != record["frame"]:
                sentence = " ".join(tree(record["tree"]).leaves()) if record["tree"] else "()"
                return f"{sentence!r}:\n    expected {short(record['frame'])}\n    got      {short(actual)}"
            return None

        self.check_all(load("semantic.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
