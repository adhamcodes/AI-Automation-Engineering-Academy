# Module 1.3 — JSON and Message Bodies

## Capability
Read, create, and reshape JSON payloads without confusing strings, numbers, booleans, arrays, objects, or null values.

## Mental model
JSON is a **serialized data format**: a standardized textual representation that programs in many languages can exchange.

Example:
```json
{
  "lead_id": 1842,
  "name": "Amina",
  "qualified": true,
  "tags": ["demo", "enterprise"],
  "owner": null
}
```

Types shown here:
- string: `"Amina"`
- number: `1842`
- boolean: `true`
- array: `[ ... ]`
- object: `{ ... }`
- null: `null`

## The automation trap
These are not equivalent:
```json
{"active": true}
```
```json
{"active": "true"}
```
The second contains a string. Many real integrations fail because the payload *looks* right to a human but violates the schema.

## Request and response bodies
A `POST` might send:
```json
{"email": "a@example.com", "plan": "pro"}
```
The server might return:
```json
{"id": "cus_901", "status": "created"}
```
Your workflow must understand both contracts independently.

## Practice
Given:
```json
{
  "orders": [
    {"id": 1, "total": 29.5, "paid": true},
    {"id": 2, "total": 18, "paid": false}
  ]
}
```
Answer:
1. What is the type of `orders`?
2. What is the type of `orders[0]`?
3. What is the type of `paid`?
4. What path would you use to access the second order's total?

## Debugging task
An API expects `quantity` as a number but your workflow emits `"3"`. Explain why validation may fail and where you would fix the transformation.

## Mastery
You can translate a small domain object into valid JSON and spot type-shape mismatches before blaming the API.
