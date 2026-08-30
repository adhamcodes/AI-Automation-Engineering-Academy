# Module 1.1 — Client, Server, and the HTTP Conversation

## Capability
Explain what happens when one program asks another program for data or an action, and trace a basic HTTP request from client to server and back.

## Mental model
Think of HTTP as a **message exchange with a contract**:

`client → request → server → response → client`

The client initiates. The server decides how to interpret the request and returns a response. The response can contain data, confirmation, or an error.

An automation tool, Python script, mobile app, browser, or Postman can all be HTTP clients. The server does not care whether the caller has a pretty UI; it cares whether the request follows the contract.

## Core ideas
- **Client:** program initiating the request.
- **Server:** program listening for requests and producing responses.
- **URL/endpoint:** address of the resource or operation.
- **Request:** method + URL + headers + optional body.
- **Response:** status + headers + optional body.
- **Statelessness:** each HTTP request is conceptually independent; applications add state using tokens, cookies, databases, IDs, etc.

## Trace this
A workflow needs customer `42` from an API.

1. Client sends `GET https://api.example.com/customers/42`.
2. Server receives the request and checks route/authentication.
3. Server loads customer 42.
4. Server responds with status `200` and JSON.
5. Workflow parses the JSON and continues.

Now change one fact: customer 42 does not exist. The network still works. The server may correctly return a `404`. **A non-200 response is not automatically a network failure.**

## Common mistakes
- Treating "API" as a magic database rather than a contract exposed by software.
- Assuming every failed business operation is a broken internet connection.
- Thinking the browser is special. It is simply one kind of client.
- Ignoring the response status and using only the response body.

## Active practice
Draw the client/request/server/response loop for:
1. a form submission;
2. an n8n HTTP Request node calling a CRM;
3. a payment provider calling your webhook.

For each, label who initiates the request.

## Transfer question
A service says, "We will notify your URL whenever an invoice is paid." Who is the client at notification time: your system or the service?

## Mastery
You can explain the flow without using the words "it just connects".
