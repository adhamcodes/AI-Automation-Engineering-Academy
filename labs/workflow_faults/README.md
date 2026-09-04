# Workflow Failure Lab

Build one workflow in n8n or another platform that accepts a customer event and writes a normalized record.

Inject these failures one at a time:

- missing required field,
- malformed JSON,
- duplicate event ID,
- downstream 429,
- downstream 503,
- partial success after one step already changed state.

For each failure record: detection signal, retry decision, idempotency behavior, human escalation, and final state.

Pass when replaying the same event cannot silently create duplicate business effects.
