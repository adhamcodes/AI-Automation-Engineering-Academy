# Module 1.7 — Rate Limits

## Capability
Design an integration that respects service limits rather than working during testing and collapsing under real volume.

## Mental model
A rate limit is a service's traffic budget or protection policy. It may limit requests per second/minute/day, concurrent requests, expensive endpoints, tokens, or user/application combinations.

A `429 Too Many Requests` usually means the caller exceeded a limit. Some APIs provide headers such as remaining quota, reset time, or `Retry-After`.

## Design responses
- slow down intentionally;
- batch requests where the API supports it;
- cache repeated reads;
- queue work rather than firing everything simultaneously;
- honor documented retry/reset headers;
- spread scheduled jobs;
- distinguish per-user vs per-app limits.

## Estimation exercise
You need to process 12,000 contacts. The API allows 120 requests/minute and each request processes one contact.

Ignoring failures, what is the theoretical minimum time? What changes if the API supports batches of 50 contacts per request?

The arithmetic is simple. The engineering lesson is not: **architecture can change your rate-limit problem dramatically.**

## Common mistake
"Add a 1-second wait node" is not a universal rate-limit strategy. Limits may be dynamic, burst-based, per endpoint, or communicated by headers.

## Mastery
You can find the documented limit, estimate throughput, and propose a design that remains inside it.
