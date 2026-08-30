# Module 2.8 — Error Workflows, Retries, and Recovery

## Capability
Encode explicit failure paths instead of hoping the workflow succeeds forever.

Apply Phase 1 classification:
- invalid input;
- expected business exception;
- transient dependency failure;
- permanent/investigation failure.

## Recovery architecture
A useful production path can include:
- bounded retry;
- error workflow;
- failure record with safe context;
- alert;
- replay mechanism;
- deduplication/idempotency protection.

## Practice
Create a simulated API step that fails for selected records. Route retryable failures to bounded retry and non-retryable records to a manual-review dataset. Prove a replay does not duplicate successful effects.

## Mastery
You can answer: "What happens to this exact item if node 7 fails at 3 AM?"
