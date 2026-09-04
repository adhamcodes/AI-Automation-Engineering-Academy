# Production Reliability Boss Fight

This is no longer an imaginary evaluator.

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

Optional extension: containerize the service and repeat the same fault run after a restart to prove state/recovery behavior.
