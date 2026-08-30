# Module 1.8 — Retries and Backoff

## Capability
Retry transient failures without creating retry storms, duplicate side effects, or endless loops.

## Not every failure deserves a retry
Often retryable:
- temporary network interruption;
- selected `5xx` responses;
- `429` when the service tells you to wait.

Usually not fixed by retrying the same request unchanged:
- malformed JSON;
- missing required field;
- invalid credential;
- permission failure.

The API's documentation is authoritative.

## Backoff
Instead of retrying instantly:
```text
attempt 1 → wait 1s
attempt 2 → wait 2s
attempt 3 → wait 4s
...
```
This is exponential backoff. Production systems often add **jitter** (small randomness) so many clients do not retry at exactly the same moment.

## Retry budget
Every retry strategy needs a stop condition:
- maximum attempts;
- maximum elapsed time;
- deadline;
- dead-letter/manual-review path.

## Dangerous case
You send `POST /payments` and the connection times out. Did the server fail before charging the card, or did it charge successfully and your response get lost?

Blind retry can charge twice unless the operation has an idempotency mechanism.

That is why the next module matters.

## Practice
Design a retry policy for:
1. GET customer profile;
2. POST a non-idempotent purchase operation;
3. 429 with Retry-After;
4. 400 validation error.

## Mastery
You can explain **why** something is retryable and define a finite retry policy.
