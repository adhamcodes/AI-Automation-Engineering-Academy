# Workflow Failure Lab

Start with the controlled n8n fixture at [`n8n/duplicate-event-starter.workflow.json`](n8n/duplicate-event-starter.workflow.json), or reproduce the same exercise in another workflow platform.

The n8n fixture contains a Manual Trigger and Code node that emits three events: two with the same `event_id` and one distinct event. Import it into a disposable n8n workspace, inspect every node before running it, then extend it into a workflow that writes a normalized record or applies another harmless business effect.

Inject these failures one at a time:

- missing required field,
- malformed JSON,
- duplicate event ID,
- downstream 429,
- downstream 503,
- partial success after one step already changed state.

For each failure record: detection signal, retry decision, idempotency behavior, human escalation, and final state.

Do not solve duplication by merely deleting one sample item. The workflow must remain safe if the same event is delivered again later.

Pass when replaying the same event cannot silently create duplicate business effects and you can explain where state/deduplication belongs.
