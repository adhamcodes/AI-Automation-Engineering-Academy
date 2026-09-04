from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_target(path: str):
    spec = importlib.util.spec_from_file_location("learner_solution", Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solution")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(path: str) -> None:
    module = load_target(path)
    processor = module.Processor()
    first = processor.process("evt-1", 10)
    second = processor.process("evt-1", 10)
    third = processor.process("evt-2", 5)
    assert first["total"] == 10, first
    assert second["total"] == 10, "duplicate event changed state"
    assert third["total"] == 15, third
    print("IDEMPOTENCY LAB: PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python evaluator.py solution.py")
    evaluate(sys.argv[1])
