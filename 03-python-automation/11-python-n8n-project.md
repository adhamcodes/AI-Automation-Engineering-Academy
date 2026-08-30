# Phase 3 Project — Hybrid Automation Service

Build a system where n8n orchestrates the process and a Python service performs logic that would be awkward/unmaintainable as canvas expressions.

## Required architecture
- n8n receives/schedules work;
- n8n calls your FastAPI service;
- Python validates/transforms data and optionally calls one practice API;
- configuration/secrets are externalized;
- explicit timeouts/retries;
- structured logs/run IDs;
- test suite for pure logic + API endpoint;
- n8n error path for service unavailable/invalid response.

## Deliverables
`ARCHITECTURE.md`, workflow export, Python package, tests, `RUNBOOK.md`, sanitized demo evidence.

## Defense
Explain why each responsibility belongs in n8n or Python. "Because I know Python" is not an architectural reason.
