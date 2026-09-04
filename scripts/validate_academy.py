from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PHASES = [
    "00-automation-thinking", "01-http-apis-webhooks", "02-workflow-engineering",
    "03-python-automation", "04-data-persistent-systems", "05-javascript-automation",
    "06-ai-powered-automation", "07-business-systems", "08-browser-document-automation",
    "09-agentic-automation", "10-production-reliability", "11-commercial-engineering",
    "12-automation-products",
]
LABS = [
    "process_spec", "http_api_lab", "workflow_faults", "python_service_lab",
    "idempotency_lab", "sql_state_lab", "js_async", "ai_eval_lab",
    "business_system_case", "browser_lab", "agent_lab", "production_boss_fight",
    "commercial_handoff", "productization",
]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    for required in ("README.md", "START-HERE.md", "ROADMAP.md", "SELF_STUDY_SYSTEM.md", "LAB_MAP.md"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")
    for phase in PHASES:
        folder = ROOT / phase
        for name in ("README.md", "RESOURCES.md", "ASSESSMENT.md"):
            if not (folder / name).is_file():
                errors.append(f"missing phase file: {phase}/{name}")
    for lab in LABS:
        if not (ROOT / "labs" / lab / "README.md").is_file():
            errors.append(f"missing lab README: labs/{lab}/README.md")

    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            raw = match.group(1).strip()
            if not raw or raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(raw.split(maxsplit=1)[0].strip("<>")).split("#", 1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repo: {md.relative_to(ROOT)} -> {raw}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {md.relative_to(ROOT)} -> {raw}")

    if errors:
        print("ACADEMY QUALITY: FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("ACADEMY QUALITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
