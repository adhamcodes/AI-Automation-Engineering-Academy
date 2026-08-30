# Module 2.2 — Expressions and Data Mapping

## Capability
Map fields safely between nodes and distinguish literal text from evaluated expressions.

## Core idea
Integrations rarely have matching schemas. One service may return `first_name`; another expects `firstName`; a third expects a nested object. Mapping is deliberate translation.

Example source:
```json
{"first":"Amina","last":"Rahman","plan":"pro"}
```
Target:
```json
{"name":"Amina Rahman","metadata":{"tier":"pro"}}
```

Expressions let a field depend on incoming data. The engineering problem is larger than syntax: missing fields, null values, arrays, and types must be handled intentionally.

## Practice
Create mappings that:
- combine first/last name;
- convert a numeric string to a number where required;
- default an absent optional field;
- preserve a stable source ID for later deduplication.

## Common failure
A beautiful expression that crashes whenever an optional nested object is missing is not robust mapping.

## Mastery
You can explain source schema → transformation → destination schema and test edge cases.
