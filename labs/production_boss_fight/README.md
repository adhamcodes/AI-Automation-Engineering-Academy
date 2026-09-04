# Production Reliability Boss Fight

This is a real production-reliability gate with three independent checks: live HTTP fault injection, durable-state evaluation, and a buildable container.

## Part 1 — Live service failures

Run the local service:

```bash
python service.py
```

In another terminal run:

```bash
python fault_injector.py
```

The injector sends:

- a valid event,
- the same event twice,
- malformed JSON,
- an event missing its ID.

Your production version must preserve idempotency, return explicit errors, persist enough state to explain what happened, and expose a useful health check.

## Part 2 — Restart-safe durable state

`broken_processor.py` is intentionally wrong because its state does not survive a fresh process instance.

Copy it to `solution.py`, repair it without editing the evaluator, then run:

```bash
python evaluator.py solution.py
```

The evaluator creates fresh `Processor` instances against the same state path and verifies that:

- duplicate events cannot change business state after a restart,
- accumulated state survives multiple restarts,
- new events continue correctly from durable state,
- an empty event ID is rejected explicitly.

## Part 3 — Container boundary

A Dockerfile is provided and the academy CI builds it, boots it, and probes `/health` on every change.

Run the same boundary locally:

```bash
docker build -t automation-boss .
docker run --rm -p 8088:8088 automation-boss
```

Then open `http://127.0.0.1:8088/health` or run the fault injector from another terminal.

## Pass condition

Pass the HTTP fault run and restart/idempotency evaluator, prove the container health check, then document the failure mode, repair, state model, recovery behavior, and remaining production risks.
