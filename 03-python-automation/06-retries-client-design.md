# Module 3.6 — Retryable Client Functions

## Capability
Encode bounded retries around explicitly retryable failures.

Build a reusable API client function with:
- timeout;
- max attempts;
- exponential backoff + optional jitter;
- 429 `Retry-After` support when documented;
- selected 5xx/network retry;
- no blind retry for validation/auth failures;
- idempotency requirement for side-effecting operations.

## Practice
Write a fake transport that returns `[503, 503, 200]` and test retry behavior without depending on the real internet. Then test `[400]` and prove no pointless retries happen.

## Mastery
Retry behavior is testable policy, not scattered `sleep()` calls.
