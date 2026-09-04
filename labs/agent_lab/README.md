# Bounded Agent Debug Lab

`broken_agent.py` intentionally performs a consequential action without approval.

Copy it to `solution.py`, repair the policy, and run:

```bash
python evaluator.py solution.py
```

Rules:

- read-only lookup may run directly,
- sending a report requires approval,
- deleting data requires approval and must be deny-by-default if approval is absent.
