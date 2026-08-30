# Module 2.9 — Debugging Execution History

## Capability
Debug workflows by evidence rather than editing nodes until the red icon disappears.

## Debugging sequence
1. reproduce or identify failing execution;
2. find first unexpected node;
3. inspect input data;
4. inspect node configuration/request;
5. inspect output/error/status;
6. compare against contract;
7. isolate external API in Postman if necessary;
8. change one hypothesis at a time;
9. rerun with a known test case.

## Practice
Deliberately introduce five failures: wrong field path, wrong type, invalid auth, wrong branch boundary, and malformed endpoint. For each, write evidence → hypothesis → fix.

## Mastery
Your debugging notes show causal reasoning, not a list of random changes.
