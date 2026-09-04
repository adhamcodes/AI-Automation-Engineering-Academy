# Production Reliability Boss Fight

This is a real production-reliability gate with two independent checks: live HTTP fault injection and durable-state evaluation.

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

## Pass condition

Pass both the HTTP fault run and the restart/idempotency evaluator, then document the failure mode, repair, state model, recovery behavior, and remaining production risks.

Optional extension: containerize the service and repeat the live fault run after a real container restart.
