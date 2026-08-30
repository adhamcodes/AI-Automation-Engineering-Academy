# Module 04.9 — Queues & Workers

## Capability
Separate asynchronous work and control retries/backpressure.

## Core model
Queues buffer work; workers process it. Delivery may be at-least-once, so consumers need idempotency and failure/dead-letter policies.

## Practice
Simulate producer/worker or use a simple queue system.

## Failure / debugging task
Handle poison job and worker crash after side effect.

## Evidence to save
Queue lifecycle diagram + worker test.

## Mastery
You can explain acknowledgement/retry semantics.
