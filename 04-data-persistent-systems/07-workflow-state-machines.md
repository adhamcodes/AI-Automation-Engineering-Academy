# Module 04.7 — Workflow State Machines

## Capability
Represent long-running process status explicitly.

## Core model
State such as pending/processing/waiting_approval/completed/failed plus allowed transitions prevents ambiguous boolean soup.

## Practice
Model an onboarding or order workflow as states/transitions.

## Failure / debugging task
Reject impossible transition such as completed→processing without explicit reopen.

## Evidence to save
State-transition function/table + tests.

## Mastery
Restarted workflow knows what remains to do.
