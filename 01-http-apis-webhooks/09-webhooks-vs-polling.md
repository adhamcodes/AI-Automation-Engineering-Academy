# Module 1.9 — Webhooks vs Polling

## Capability
Choose an event-delivery pattern based on latency, reliability, availability, and provider capability.

## Polling
Your system repeatedly asks:
> "Anything new?"

Example: every five minutes call `GET /orders?updated_since=...`.

Advantages:
- works when provider has no webhook system;
- your system controls schedule;
- conceptually simple.

Costs:
- wasted requests when nothing changed;
- delay up to polling interval;
- pagination/state complexity;
- rate-limit pressure.

## Webhooks
Provider sends an HTTP request to a URL you expose when an event occurs.

Example:
> payment provider → `POST https://your-system.example/webhooks/payment-paid`

Advantages:
- near-real-time;
- fewer useless requests;
- natural event-driven design.

Costs:
- your endpoint must be reachable;
- deliveries may be duplicated or arrive out of order;
- you must authenticate/verify the sender according to provider docs;
- you need failure/retry handling.

## Critical misconception
A webhook delivery is not automatically "exactly once". Design consumers so duplicate delivery does not duplicate business effects.

## Design exercise
Choose webhook, polling, or hybrid for:
- hourly weather snapshot;
- payment confirmation;
- service that provides no webhooks;
- critical inventory sync where webhook delivery can be missed.

Explain the tradeoff, not just the answer.

## Mastery
You can draw both patterns and explain who initiates each HTTP request.
