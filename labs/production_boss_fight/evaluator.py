from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("production_solution", Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solution")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(path: str) -> None:
    module = load(path)
    with tempfile.TemporaryDirectory() as temp:
        state_path = str(Path(temp) / "state.db")

        first_process = module.Processor(state_path)
        first = first_process.process("evt-1", 10)
        assert first["total"] == 10, first

        # Simulate a process restart by constructing a fresh instance against the same state path.
        after_restart = module.Processor(state_path)
        duplicate = after_restart.process("evt-1", 10)
        assert duplicate["total"] == 10, "duplicate changed durable business state after restart"

        second = after_restart.process("evt-2", 5)
        assert second["total"] == 15, second

        second_restart = module.Processor(state_path)
        third = second_restart.process("evt-3", 7)
        assert third["total"] == 22, "state did not survive a second restart"

        try:
            second_restart.process("", 1)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("empty event_id must be rejected")

    print("PRODUCTION RESTART/IDEMPOTENCY GATE: PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python evaluator.py solution.py")
    evaluate(sys.argv[1])
