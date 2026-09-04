from __future__ import annotations

import json
from pathlib import Path


def baseline(text: str) -> str:
    lowered = text.lower()
    high_consequence = ("refund", "delete", "payment", "charge")
    return "human_review" if any(word in lowered for word in high_consequence) else "automate"


def score(cases_path: Path) -> tuple[int, int]:
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    correct = sum(baseline(case["input"]) == case["expected"] for case in cases)
    return correct, len(cases)


if __name__ == "__main__":
    correct, total = score(Path(__file__).with_name("cases.json"))
    print(f"baseline: {correct}/{total}")
