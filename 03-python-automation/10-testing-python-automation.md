# Module 3.10 — Testing Automation Code

## Capability
Test business logic and service behavior without requiring every external service to be live.

Testing layers:
- pure function/unit tests;
- file fixture tests;
- fake/mocked transport tests;
- FastAPI endpoint tests;
- a small number of real integration tests where safe.

Test failures as seriously as happy paths: timeout, malformed JSON, missing file, 429, invalid input.

## Practice
Create tests for your Phase 3 API client and normalization service. At least half the test cases should be failure/boundary cases.

## Mastery
You can change implementation and use tests to prove behavior stayed correct.
