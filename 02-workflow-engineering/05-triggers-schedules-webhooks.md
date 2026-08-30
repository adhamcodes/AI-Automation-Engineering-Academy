# Module 2.5 — Triggers, Schedules, and Webhooks

## Capability
Choose and configure how a workflow begins, then reason about timing, duplicate delivery, and test-vs-production endpoints.

Common starts:
- manual trigger for development;
- schedule trigger for periodic jobs;
- webhook trigger for incoming events;
- app/service triggers provided by integrations.

A trigger defines more than convenience. It changes reliability assumptions.

## Practice
Implement one process in two ways:
1. scheduled polling every 10 minutes;
2. webhook event reception.

Compare latency, API volume, failure detection, and recovery.

## Webhook discipline
- verify provider authentication/signature if supported;
- acknowledge within provider timeout expectations;
- separate immediate acknowledgement from long work when necessary;
- deduplicate repeated events;
- store event IDs/status for critical flows.

## Mastery
You choose a trigger based on system behavior, not because it is the first node in the menu.
