# Module 3.8 — FastAPI Service Fundamentals

## Capability
Expose custom Python logic through a small typed HTTP API that another workflow can call.

Learn only the service fundamentals needed now:
- app and route/path operation;
- GET/POST;
- path/query/body inputs;
- validation models;
- status/errors;
- automatic OpenAPI docs;
- configuration;
- basic tests.

## Practice
Expose your lead-normalization function as `POST /normalize-lead`. Invalid input must produce a useful client error; valid input returns a documented schema.

## Boundary
Do not build authentication providers, microservice fleets, or cloud infrastructure yet. Phase 10 handles production security/deployment.

## Mastery
You can turn pure Python logic into a small documented service and test it independently.
