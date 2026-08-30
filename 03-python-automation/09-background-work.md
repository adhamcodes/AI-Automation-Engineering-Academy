# Module 3.9 — Background Work and Boundaries

## Capability
Know when an HTTP request should finish quickly and work should continue separately.

FastAPI can run small background tasks after responding, but heavy/reliable distributed work typically needs a queue/worker architecture introduced later.

Use this distinction:
- small post-response side task → local background mechanism may be fine;
- long/heavy/retry-critical job → persist job state and use a proper worker/queue later.

## Practice
Design an endpoint accepting a document-processing request. Return a job ID quickly. Sketch how status would be queried. Do not fake durability before Phase 4.

## Mastery
You can explain why "run a 20-minute task inside the webhook request" is fragile.
