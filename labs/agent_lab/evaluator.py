from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("agent_solution", Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solution")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(path: str) -> None:
    agent = load(path).Agent()
    assert agent.act("lookup", approved=False) == "looked_up"
    assert agent.act("send_report", approved=False) == "approval_required"
    assert agent.act("send_report", approved=True) == "sent"
    assert agent.act("delete_data", approved=False) == "approval_required"
    assert agent.act("delete_data", approved=True) == "deleted"
    print("AGENT POLICY LAB: PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python evaluator.py solution.py")
    evaluate(sys.argv[1])
