# Phase 1 Mastery Assessment — HTTP/API Integration

**Mode:** closed-solution assistance. Official documentation and general references are allowed. AI-generated solution steps are not.

## Part A — Explain
Without notes, explain:
1. request vs response;
2. 401 vs 403;
3. 400 vs 500;
4. webhook vs polling;
5. retry vs idempotency;
6. why JSON `true` differs from `"true"`.

## Part B — Diagnose
You receive five failures:
- `429` after a burst;
- `401` after an hour;
- duplicate webhook delivery;
- pagination returning the same page forever;
- POST timeout with unknown server outcome.

For each, identify the likely class of problem, evidence to inspect, and a safe response.

## Part C — Transfer build
Use a small unfamiliar API that you have not used in the lessons. From official docs only:
- make one authenticated request if a free/safe auth option exists, otherwise use an unauthenticated practice API;
- demonstrate one query/path parameter;
- handle pagination if available;
- intentionally trigger and explain one error;
- document a rate-limit/retry strategy;
- identify whether any write action requires idempotency protection.

## Pass standard
Pass only if you can both **make the integration work** and **explain why it works**. A copied request with no understanding is a fail.

## Repair loop
If you fail one competency, redo only that competency:
- HTTP semantics → Modules 1.1–1.3 + 5 trace drills
- docs/auth → Modules 1.4–1.5 + new contract extraction
- pagination/rate limits → Modules 1.6–1.8 + one simulated workload
- event reliability → Modules 1.9–1.11 + duplicate-delivery design
