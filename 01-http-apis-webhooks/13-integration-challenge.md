# Phase 1 Integration Challenge — Unfamiliar API

## Scenario
You are given documentation for a small API you have not used before. Your task is to retrieve a collection, filter it using a documented parameter, and create or update one resource if the API supports safe write operations.

## Deliverables
Create an `integration-lab/` folder containing:
- `CONTRACT.md` — method/URL/auth/parameters/body/status/pagination/rate-limit notes;
- exported/saved request definitions or screenshots with secrets removed;
- `FAILURE_PLAN.md` — how 400/401/403/404/429/5xx are handled where relevant;
- `PAGINATION.md` — exact termination rule if pagination exists;
- `RELIABILITY.md` — retry/idempotency choices;
- `REFLECTION.md` — what the docs left ambiguous and how you verified it.

## Constraints
- Never commit a real credential.
- Do not follow a tutorial for this exact API.
- You may use the API's official documentation and general HTTP references.
- If the API requires payment or sensitive data, choose a safe alternative.

## Pass criteria
You can demonstrate the integration, explain every part of the request, and defend what happens when the happy path fails.
