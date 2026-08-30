# Phase 2 Mastery Assessment — Useful Workflow Builder

**Mode:** no AI-generated workflow solution. Official n8n documentation and Phase 1 HTTP references are allowed.

You receive a short process specification for a fictional operations team. Build the workflow from an empty canvas.

The specification must require:
- one event/schedule trigger;
- mapping between mismatched schemas;
- branching with boundary cases;
- multi-item processing;
- one unfamiliar HTTP API call;
- a reusable sub-workflow;
- explicit transient vs permanent failure handling;
- configuration/credential separation;
- documentation.

## Oral/written defense
Explain:
- data shape after each major stage;
- why each branch is exclusive or independent;
- retry/idempotency decisions;
- how you would debug one injected failure;
- what must change before this becomes production/client-grade.

## Pass
Pass when the workflow works across test cases *and* you can defend its architecture. Template imitation without explanation fails.
