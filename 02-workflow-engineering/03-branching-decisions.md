# Module 2.3 — Branching and Decision Logic

## Capability
Turn business rules into explicit branches without creating contradictory or unreachable paths.

## Mental model
A branch is a decision table encoded into workflow control flow.

Before adding IF/Switch nodes, write the rules in plain language.

Example:
- if score >= 80 and country supported → priority lead;
- else if score >= 50 → normal review;
- else → nurture queue.

Then test boundaries: 49, 50, 79, 80.

## Independent vs exclusive decisions
Two separate IF nodes may both run. An exclusive classification should have mutually exclusive outcomes. Decide which model your business rule requires.

## Practice
Design a routing workflow for orders based on value, payment status, and fraud-review flag. Create a small decision table first, then implement it.

## Mastery
You can prove each rule has the intended path and boundary behavior.
