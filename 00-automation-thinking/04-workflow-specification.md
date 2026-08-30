# Module 0.4 — Write a Workflow Specification

## Goal
Describe an automation clearly before opening n8n or writing Python.

## Minimal specification
- objective
- trigger
- inputs
- systems involved
- decision rules
- outputs
- state that must persist
- expected failures
- retry behavior
- duplicate/idempotency concerns
- human approval points
- success metric
- security/privacy notes

## Practice specification
Create a specification for this fictional system:

> A small clinic receives appointment requests from a web form. Staff currently copy them into a spreadsheet and send confirmations manually. Some requests are duplicates, some omit a phone number, and urgent messages should be reviewed by a person before any automated reply.

Do not use AI to generate the first draft.
