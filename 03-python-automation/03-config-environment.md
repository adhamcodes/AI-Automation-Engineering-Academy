# Module 3.3 — Configuration and Environment Variables

## Capability
Separate code from values that change by environment or must remain secret.

Categories:
- source-controlled defaults that are safe;
- environment-specific config;
- secrets;
- runtime business input.

Environment variables are common for deployment config/secrets, but they are strings and can be missing/malformed. Validate them at startup.

## Practice
Refactor a script containing hardcoded token, API URL, output directory, timeout, and threshold. Decide which belong in environment/config/CLI/business input.

Create a startup validator that fails with a useful message when required config is missing.

## Mastery
You can move the same code between local/test/production-like environments by changing configuration, not source code.
