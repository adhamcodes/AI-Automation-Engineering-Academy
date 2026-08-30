# Phase 2 Project — Lead Intake Orchestrator

Build a realistic workflow that receives a lead, validates/normalizes fields, assigns a category, calls at least one safe practice API, writes a final normalized record to a simple phase-appropriate sink (for example an n8n Data Table or local file; do not introduce database architecture yet), and sends/records a notification result.

## Required engineering behavior
- clear trigger contract;
- schema mapping;
- at least three exclusive routing outcomes;
- reusable normalization sub-workflow;
- credentials/config separated from business data;
- bounded error path;
- safe replay/idempotency strategy;
- descriptive names and workflow documentation;
- execution test cases for happy path and at least four failures.

## Deliverables
- workflow export with secrets removed;
- `ARCHITECTURE.md`;
- `TEST_CASES.md`;
- `FAILURE_RECOVERY.md`;
- one short demo recording or screenshots if you want portfolio evidence.

## Commercial interpretation
This is still a simulated internal system. Do not market yourself as a production automation engineer until later reliability/data phases are passed.
