# Module 2.1 — Workflow Execution and Data Items

## Capability
Trace exactly what data enters a node, what leaves it, and how multiple items propagate through a workflow.

## Mental model
A visual canvas can hide a program. Treat each node as a transformation with an input contract and an output contract.

A workflow is easier to reason about when you ask three questions at every step:
1. What items arrive here?
2. What fields does this node read/change/create?
3. How many items leave?

In n8n, workflow data is commonly represented as items containing JSON-like fields. A node may receive one item, many items, or no item depending on execution history and branching.

## Practice
Build a tiny workflow that starts with three sample records, adds a normalized `full_name`, and outputs only `id`, `full_name`, and `email`.

Before running it, write the expected item count and shape after each node. Compare prediction to execution.

## Debugging habit
When downstream data is wrong, inspect the **first node where shape diverges from your prediction**. Do not randomly edit the final node.

## Mastery
You can narrate data flow through a workflow without saying "the node somehow gets it."
