# Module 04.2 — SQL CRUD Safely

## Capability
Read/write state with parameterized SQL and explicit intent.

## Core model
SELECT/INSERT/UPDATE/DELETE manipulate persistent state; parameterization separates data from SQL and avoids injection/string-escaping errors.

## Practice
Implement CRUD against a local Postgres/SQLite practice DB.

## Failure / debugging task
Repair unsafe string-formatted query and accidental mass update.

## Evidence to save
Small data-access module + tests.

## Mastery
Writes target correct rows and inputs are parameterized.
