# Module 1.11 — Error Handling as a System

## Capability
Classify failures and design explicit paths for recovery, rejection, retry, and human attention.

## Four useful categories
1. **Invalid input** — caller/data violates contract.
2. **Expected business exception** — e.g. customer not found, payment declined.
3. **Transient technical failure** — timeout, temporary dependency outage.
4. **Permanent/investigation failure** — permission/configuration/schema mismatch, repeated unknown error.

Do not treat all four as "workflow failed".

## Error contract
For an integration, decide:
- what counts as success;
- which failures branch normally;
- which retry;
- how many retries;
- what is logged;
- what context is safe to log;
- when a human is alerted;
- how failed work can be replayed;
- how duplicate replay is prevented.

## Useful context in logs
- correlation/request ID;
- workflow/job ID;
- endpoint/action;
- status/error category;
- attempt number;
- safe domain identifiers.

Avoid logging secrets, full tokens, or sensitive payloads without a justified policy.

## Debugging exercise
A workflow fails 3% of the time. The only log message is "HTTP error". List the additional evidence you would want before changing the workflow.

## Mastery
You can design an error path before production rather than adding random retries after incidents.
