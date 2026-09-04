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
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("API-secret-like token", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
]
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sql", ".html", ".js", ".csv"}


def validate_hygiene(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
            continue
        relative = path.relative_to(ROOT)
        if path.stat().st_size == 0:
            errors.append(f"unexpected empty file: {relative}")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and not path.name.endswith(".workflow.json"):
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".md":
            match = PLACEHOLDER.search(text)
            if match:
                errors.append(f"placeholder marker {match.group(0)!r} in {relative}")
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible {label} committed in {relative}")


def main() -> int:
    errors: list[str] = []
    for required in (
        "README.md", "START-HERE.md", "ROADMAP.md", "SELF_STUDY_SYSTEM.md",
        "PARALLEL_STUDY.md", "LAB_MAP.md",
    ):
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

    validate_hygiene(errors)

    if errors:
        print("ACADEMY QUALITY: FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("ACADEMY QUALITY: PASS")
    print("Verified phase/lab structure, local links, placeholders, empty files, and secret-pattern hygiene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
