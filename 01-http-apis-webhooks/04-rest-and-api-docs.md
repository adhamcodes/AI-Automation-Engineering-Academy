# Module 1.4 — REST Conventions and Reading API Documentation

## Capability
Open unfamiliar API documentation and extract the minimum contract required to make a correct call.

## Do not worship REST
"REST" describes architectural conventions, but real APIs vary. Your job is not to grade the API's purity. Your job is to understand its contract safely.

## Documentation extraction checklist
For any endpoint, find:
1. base URL;
2. path;
3. HTTP method;
4. authentication method;
5. required headers;
6. path/query parameters;
7. request-body schema;
8. success response;
9. error responses;
10. pagination/rate-limit rules;
11. idempotency requirements if the operation creates side effects.

## Example
Suppose docs say:

`POST /v1/tickets`

Required body:
```json
{"subject": "string", "priority": "low|normal|high"}
```

Before touching Postman, you should be able to write a request plan:
- method: POST
- endpoint: `<base>/v1/tickets`
- auth: find docs
- content type: likely JSON, verify
- valid priority values: exactly three documented values
- expected successful status: verify

## Query vs path
`GET /users/42` often identifies one resource by path.

`GET /users?status=active&page=2` commonly filters/paginates with query parameters.

These are conventions, not physics.

## Exercise — Documentation archaeology
Choose a public practice API or an API you already have access to. Without sending a request, write a one-page integration contract using the checklist above. Then send the request and compare reality against your prediction.

## Mastery
You can make an "integration contract" before opening a workflow canvas.
