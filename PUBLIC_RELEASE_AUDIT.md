# Public Release Audit

Repository: **AI Automation Engineering Academy**

## Current rebuild verification — 2026-09-04

The release gate is now executable and continuous rather than a one-time Markdown scan.

GitHub Actions verifies on both Linux and Windows using Python 3.12 and 3.14:

- all 13 phase directories and required phase files exist,
- every controlled lab mapped by `LAB_MAP.md` exists,
- local Markdown links resolve inside the repository,
- actionable TODO/TBD/FIXME placeholders are rejected,
- unexpected empty files are rejected,
- common committed-secret patterns are rejected,
- dependency-free lab smoke tests pass,
- known-broken idempotency, agent, and production implementations are rejected by their evaluators,
- n8n workflow fixtures satisfy the repository workflow contract,
- the production boss-fight Docker image builds, boots, and serves a valid health response.

The rebuild also ships stable local fixtures for API failures, duplicate webhooks, n8n workflows, browser automation, AI evaluation, approval boundaries, and production recovery so critical assessments no longer depend on imaginary infrastructure.

### Result

**PASS** when the current `Academy quality gates` workflow is green. A green workflow proves the checks above; it does not claim that external resources can never change or that every possible learner implementation is correct.

## Historical v1.0 audit

Before the executable rebuild, the v1.0 publication audit scanned **208 Markdown files** across **13 phase directories** and reported zero broken local links, curriculum placeholder markers, credential-like patterns, personal-name references, or missing phase README/RESOURCES/ASSESSMENT files. It inventoried **27 external URLs**.

Those counts are preserved here as historical evidence only; they are not current file-count claims after the executable lab rebuild.
