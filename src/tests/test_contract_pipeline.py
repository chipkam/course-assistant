"""End-to-end contract over the labelled cases (§8).

Every case the reference answers correctly must stay correct; the others are
improvement targets and are only reported.  As in the graded evaluation, each
suite starts from a fresh context and runs in file order, because some cases
refer to the case just before them.
"""

import unittest

from hcmut.iaslab.nlp.app.answer import MISSING_CONTEXT, NOT_FOUND, NOT_UNDERSTOOD
from hcmut.iaslab.nlp.app.pipeline import CourseAssistant

from tests.contract_support import SRC, ContractTestCase, load, normalize, short


def query_status(trace) -> str:
    if trace.query.found:
        return "FOUND"
    if trace.query.kind in {"UNKNOWN", "UNRESOLVED_CONTEXT"}:
        return "SKIPPED"
    return "NOT_FOUND"


def mismatch(case, trace) -> str | None:
    intent = trace.detected_intent
    entity = trace.detected_entity or ("OUT_OF_SCOPE" if intent == "UNKNOWN" else "NONE")
    status = query_status(trace)
    problems = []
    if intent != case["expected_intent"]:
        problems.append(f"intent {intent} ≠ {case['expected_intent']}")
    if entity != case["expected_entity"]:
        problems.append(f"entity {entity} ≠ {case['expected_entity']}")
    if status != case["expected_query_status"]:
        problems.append(f"status {status} ≠ {case['expected_query_status']}")
    answer = normalize(trace.answer)
    missing = [term for term in case["expected_answer_terms"] if normalize(term) not in answer]
    if missing:
        problems.append(f"answer missing {missing}")
    if not case["expected_answer_terms"]:
        if status == "FOUND" and trace.answer in {NOT_FOUND, NOT_UNDERSTOOD, MISSING_CONTEXT}:
            problems.append("found but answered with a fallback")
        if status == "NOT_FOUND" and trace.answer != NOT_FOUND:
            problems.append("not found but answer is not NOT_FOUND")
    if problems:
        return f"{case['id']} {case['query']!r}: " + "; ".join(problems) + f" | {short(trace.answer, 80)}"
    return None


class PipelineContractTests(ContractTestCase):
    def setUp(self) -> None:
        self.assistant = self.build(lambda: CourseAssistant.from_root(SRC))

    def run_suites(self) -> list[tuple[dict, str | None]]:
        """Return (case, mismatch) for every case, suite by suite in file order."""
        outcomes = []
        cases = load("cases.jsonl")
        for suite in ("official", "challenge"):
            self.assistant.reset_context()
            for case in (c for c in cases if c["suite"] == suite):
                trace = self.assistant.process(case["query"], use_context=True)
                outcomes.append((case, mismatch(case, trace)))
        return outcomes

    def test_reference_passing_cases_stay_correct(self) -> None:
        outcomes = [(case, problem) for case, problem in self.build(self.run_suites) if case["reference_pass"]]
        self.check_all(outcomes, lambda outcome: outcome[1])

    def test_report_improvement_targets(self) -> None:
        targets = [(case, problem) for case, problem in self.build(self.run_suites) if not case["reference_pass"]]
        fixed = [case["id"] for case, problem in targets if problem is None]
        print(f"\nimprovement targets: {len(fixed)}/{len(targets)} fixed {fixed}")


if __name__ == "__main__":
    unittest.main()
