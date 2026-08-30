# Module 2.6 — Credentials and Configuration

## Capability
Keep secrets and environment-specific values out of workflow business logic.

## Separate three kinds of information
- **secret:** token/password/private key;
- **configuration:** base URL, environment name, timeout, feature setting;
- **business data:** lead, order, invoice, etc.

Mixing them creates insecure, unportable workflows.

Use the platform credential system for supported secrets. Use environment/configuration mechanisms appropriate to your deployment. Never export real secrets into public examples.

## Practice
Take a workflow with hardcoded API key, production URL, recipient email, and business threshold. Refactor so each belongs in the correct storage/configuration layer.

## Mastery
You can move a workflow between test and production without editing secrets into node code.
