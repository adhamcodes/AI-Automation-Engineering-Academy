# Module 3.2 — JSON, CSV, and Filesystem Automation

## Capability
Build repeatable file pipelines without corrupting source data or depending on manual edits.

Use `pathlib` for paths, standard `json`/`csv` tools when sufficient, and explicit encoding (usually UTF-8).

Pipeline mental model:
`discover inputs → validate → transform → write new output → verify → archive/report`

Prefer creating a new output and then replacing atomically when correctness matters, rather than rewriting the only copy mid-process.

## Practice
Build a folder processor that:
- finds `.json` files;
- validates required keys;
- writes normalized CSV;
- records rejected file names/reasons;
- never deletes originals;
- behaves correctly when the input folder is empty.

## Mastery
The same input set produces the same output without hand edits, and one malformed file does not destroy the whole batch.
