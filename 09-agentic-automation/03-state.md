# Module 09.3 — Agent State & Workflow State

## Capability
Keep durable business state separate from conversational reasoning.

## Core model
Store canonical workflow status/data in DB/state machine; agent context is a view, not source of truth.

## Practice
Build state transitions around a tool-using task.

## Failure / transfer task
Restart after model call and avoid repeated action.

## Evidence to save
State model + replay test.

## Mastery
System resumes without relying on hidden chat context.
