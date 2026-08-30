# Module 06.9 — Tool Calling in Workflows

## Capability
Let models propose structured actions while deterministic code validates/executes.

## Core model
Separate decision from side effect: model suggests tool + args; code checks authorization/schema/state before execution.

## Practice
Build tool proposal for CRM lookup/update.

## Failure / debugging task
Inject unauthorized/destructive tool request.

## Evidence to save
Tool validation layer.

## Mastery
Model cannot bypass deterministic permission checks.
