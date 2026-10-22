"""Contract: context resolution of the golden dialogues (§7).

Raw frames and query results come from golden files, so only DialogueContext
is under test.  The explanatory trace string is free text.
"""

import unittest

from hcmut.iaslab.nlp.app.dialogue import DialogueContext

from tests.contract_support import ContractTestCase, frame, frame_dict, load, result, short


class DialogueContractTests(ContractTestCase):
    def test_resolutions_match_golden(self) -> None:
        def check(dialogue):
            context = DialogueContext()
            for number, turn in enumerate(dialogue["turns"], start=1):
                resolved, _ = context.resolve(frame(turn["raw"]))
                if frame_dict(resolved) != turn["resolved"]:
                    return (
                        f"{dialogue['id']} U{number} {turn['sentence']!r}:\n"
                        f"    expected {short(turn['resolved'])}\n    got      {short(frame_dict(resolved))}"
                    )
                context.update(resolved, result(turn["result"]))
            return None

        self.check_all(load("dialogue.jsonl"), check)


if __name__ == "__main__":
    unittest.main()
