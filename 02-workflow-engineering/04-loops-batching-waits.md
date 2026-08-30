# Module 2.4 — Loops, Batching, and Waits

## Capability
Process collections safely while respecting API limits and avoiding accidental endless loops.

## Core idea
Do not loop merely because there are multiple items. Many nodes naturally process each incoming item. Explicit loops/batches are useful when you need controlled chunking, pagination, pacing, or iterative state.

## Batching
If an API permits 50 records/request, batching 5,000 records into groups of 50 can reduce 5,000 calls to 100.

## Waits
Waits can implement schedules, external callbacks, or pacing. A fixed delay is not a complete rate-limit strategy; Phase 1 rules still apply.

## Practice
Process 250 simulated contacts in batches of 25, with a deliberate branch for invalid contacts and a final count of success/failure.

## Safety checks
- finite termination condition;
- item/cursor changes every iteration;
- maximum iterations during development;
- idempotent/replay-safe business effects where relevant.

## Mastery
You know when the platform already iterates for you and when explicit control is justified.
