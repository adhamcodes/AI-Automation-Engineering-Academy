# Module 1.12 — API Exploration with Postman

## Capability
Use an API client as a laboratory: construct requests, inspect raw responses, vary inputs, save reproducible examples, and separate API behavior from workflow-tool behavior.

## Why this matters
When an n8n workflow fails, debugging directly inside a 30-node flow creates too many variables. First prove the API contract in isolation.

## Basic workflow
1. create an HTTP request;
2. choose method and URL;
3. add query parameters, headers, auth, and body;
4. send;
5. inspect status, headers, body, and timing;
6. deliberately send one invalid request;
7. save useful requests in a collection.

A Postman account is not required for the lightweight desktop API client; signing in adds sync/collaboration features. Use whichever mode fits your privacy/workflow.

## Lab — Contract exploration
Using a safe practice API:
- perform a GET with a query parameter;
- perform a POST with JSON if supported;
- inspect a `2xx` response;
- deliberately cause a `4xx` response;
- identify content type;
- save the requests;
- write a short `API_NOTES.md` describing the contract.

## Debugging rule
If the request works in Postman but fails in your automation tool, compare the **actual outgoing request**: method, URL, headers, query, body, auth, encoding.

If it fails in both places, stop blaming the automation canvas and investigate the API contract/network/credential.

## Mastery
You can use Postman as a controlled experiment, not merely a GUI button that says Send.
