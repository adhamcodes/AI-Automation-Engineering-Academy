# Idempotency Debug Lab

`broken_processor.py` intentionally applies the same event more than once.

Copy it to `solution.py`, repair it without editing `evaluator.py`, then run:

```bash
python evaluator.py solution.py
```

Pass when a repeated event ID does not create a second business effect and a different event still processes normally.
