# Module 04.4 — Transactions

## Capability
Keep multi-step database changes atomic where partial success would corrupt state.

## Core model
Transactions group changes into commit/rollback boundaries; isolation/concurrency determine what parallel work can observe.

## Practice
Create a two-table write that rolls back on failure.

## Failure / debugging task
Inject exception between writes and prove no half-state remains.

## Evidence to save
Transactional service function + test.

## Mastery
You choose transaction boundary from business invariant.
