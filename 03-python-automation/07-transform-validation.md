# Module 3.7 — Data Transformation and Validation

## Capability
Represent transformation rules as small testable functions and reject invalid data deliberately.

Separate:
1. parse raw input;
2. validate required structure/types;
3. normalize;
4. apply business rules;
5. serialize output.

Do not mix API calls and 80 lines of field-cleaning logic in one function.

## Practice
Normalize lead records with email, country, score, tags, and optional company. Return a result containing either normalized data or explicit validation errors. Test boundaries and missing keys.

## Mastery
Your transformation layer can be tested without n8n, network, or filesystem.
