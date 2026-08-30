# Module 2.7 — Sub-workflows and Modularity

## Capability
Break a growing automation into reusable units with explicit inputs/outputs.

## When to extract
Good candidates:
- repeated API operation;
- reusable validation;
- notification routine;
- document normalization;
- error/reporting path.

Bad reason:
> "This canvas has too many nodes so I'll split randomly."

A module should have one coherent responsibility and a contract.

## Practice
Build a reusable `normalize-contact` sub-workflow receiving contact data and returning a normalized shape plus validation status. Call it from two different parent workflows.

## Design question
What should happen if a sub-workflow changes its output schema? Treat this as an interface/versioning problem, not merely a canvas problem.

## Mastery
You can name the responsibility and contract of every extracted workflow.
