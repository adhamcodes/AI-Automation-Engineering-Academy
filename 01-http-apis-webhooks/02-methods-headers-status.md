# Module 1.2 — Methods, Headers, and Status Codes

## Capability
Read an HTTP request and predict its intended effect; read a response and decide whether the automation should continue, retry, branch, or stop.

## Methods are intent
Common methods:
- `GET` — retrieve a representation; should not be used to create side effects.
- `POST` — submit/create/trigger an operation.
- `PUT` — usually replace a resource representation.
- `PATCH` — usually partially update a resource.
- `DELETE` — request deletion.

The precise contract always comes from the API documentation. Do not infer behavior from the method alone.

## Headers are metadata
Headers carry information about the message rather than the domain object itself. Examples:
- `Authorization: Bearer ...`
- `Content-Type: application/json`
- `Accept: application/json`
- request IDs, version headers, rate-limit information

A useful distinction:
- **Body:** "Here is the customer I want to create."
- **Header:** "The body is JSON, and here is my credential."

## Status-code families
- `2xx`: request successfully processed in some form.
- `3xx`: redirection.
- `4xx`: client-side/request problem from the server's perspective.
- `5xx`: server-side failure.

Important examples:
- `200 OK` — success with a response.
- `201 Created` — resource created.
- `204 No Content` — success with no response body expected.
- `400 Bad Request` — malformed/invalid request.
- `401 Unauthorized` — authentication missing/invalid.
- `403 Forbidden` — identity known but operation not permitted.
- `404 Not Found` — target not found.
- `409 Conflict` — request conflicts with current state.
- `429 Too Many Requests` — rate limit exceeded.
- `500/502/503` — server/service failures of different kinds.

## Reasoning drill
For each response decide **retry / do not retry / investigate contract**:
- 401 after token expiration
- 400 because a required field is missing
- 429 with `Retry-After: 30`
- 503 from a normally healthy service
- 404 when looking up an optional CRM record

There is no universal answer for the 404: sometimes it is expected branching, sometimes it is an error. Reliability comes from **domain context + HTTP semantics**.

## Mastery
Given a method/status/header combination, you can explain what it tells you and what it does *not* tell you.
