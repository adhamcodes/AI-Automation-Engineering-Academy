from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = [
    ROOT / "labs/http_api_lab/test_server.py",
    ROOT / "labs/python_service_lab/test_service.py",
    ROOT / "labs/ai_eval_lab/test_evaluator.py",
]
COMPILE_ONLY = [
    ROOT / "labs/idempotency_lab/broken_processor.py",
    ROOT / "labs/idempotency_lab/evaluator.py",
    ROOT / "labs/agent_lab/broken_agent.py",
    ROOT / "labs/agent_lab/evaluator.py",
    ROOT / "labs/production_boss_fight/service.py",
    ROOT / "labs/production_boss_fight/fault_injector.py",
]

for test in TESTS:
    subprocess.run([sys.executable, test.name], cwd=test.parent, check=True)
for source in COMPILE_ONLY:
    subprocess.run([sys.executable, "-m", "py_compile", str(source)], check=True)
print("LAB SMOKE TESTS: PASS")
