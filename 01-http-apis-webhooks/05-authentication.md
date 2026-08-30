# Module 1.5 — API Keys, Bearer Tokens, and OAuth Concepts

## Capability
Recognize common API authentication patterns, place credentials correctly, and avoid exposing secrets in workflow logic or repositories.

## Authentication vs authorization
- **Authentication:** who/what are you?
- **Authorization:** what are you allowed to do?

A system can know your identity and still return `403` because you lack permission.

## API keys
Often a long secret string issued to an application/user. APIs may expect it in a header or occasionally a query parameter. Follow the documentation exactly.

Do not:
- commit keys to Git;
- paste secrets into screenshots/tutorial examples;
- hardcode them inside reusable workflow source;
- log them in plaintext.

## Bearer tokens
Common pattern:
`Authorization: Bearer <token>`

"Bearer" means possession of the token is enough to use it within its permissions and lifetime. Treat it as a secret.

## OAuth — mental model, not implementation mastery yet
OAuth commonly lets one application receive limited access to another service **without collecting the user's password**.

A simplified flow:
1. user approves access with the provider;
2. your application receives authorization material;
3. it exchanges that for an access token;
4. token carries limited scopes/permissions;
5. token may expire and require refresh.

Important words: client ID, client secret, authorization URL, token URL, redirect URI, scope, access token, refresh token.

You do not need to implement an OAuth server in Phase 1. You do need to understand why a connector asks for these fields and why redirect URLs/scopes matter.

## Security exercise
For each secret location decide acceptable/unacceptable and why:
- `.env` ignored by Git;
- n8n credential store;
- README screenshot;
- GitHub public repository;
- operating-system environment variable;
- workflow node's plain-text field exported to JSON.

## Mastery
You can configure a documented auth method without leaking credentials and explain the difference between 401 and 403.
