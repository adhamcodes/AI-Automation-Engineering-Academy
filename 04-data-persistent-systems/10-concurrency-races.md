# Module 04.10 — Concurrency & Race Conditions

## Capability
Recognize when two executions can corrupt shared state.

## Core model
Concurrent reads/writes can interleave. Use atomic DB operations, locks/constraints or compare-and-set patterns according to invariant.

## Practice
Run two workers trying to claim same job.

## Failure / debugging task
Reproduce double-processing and fix at DB boundary.

## Evidence to save
Concurrency test.

## Mastery
Correctness does not depend on “probably only one run.”
