# Module 04.8 — Idempotency & Deduplication

## Capability
Make repeated delivery safe.

## Core model
Idempotency means repeating an operation with the same logical request does not create unintended duplicate side effects. Use stable operation/event keys and stored outcomes.

## Practice
Handle duplicate webhook deliveries and retries.

## Failure / debugging task
Inject same event 5 times and prove one business action occurs.

## Evidence to save
Idempotency table/key strategy.

## Mastery
Duplicate input is expected, not exceptional.
