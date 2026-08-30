# Module 3.5 — Logging and Run Evidence

## Capability
Produce enough evidence to debug automation after it runs unattended.

Use structured, leveled logging concepts:
- DEBUG: development detail;
- INFO: normal milestones;
- WARNING: unusual but handled;
- ERROR: operation failed;
- CRITICAL: system-level intervention required.

Useful fields: run/job ID, item ID, stage, attempt, duration, result. Avoid secrets and unnecessary personal data.

## Practice
Instrument a batch job so you can answer later:
- when did it start/end?
- how many inputs?
- how many succeeded/failed/skipped?
- which identifiers failed and why?

## Mastery
A failure report is actionable without rerunning blindly.
