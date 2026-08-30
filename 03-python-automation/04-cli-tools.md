# Module 3.4 — Command-Line Automation Tools

## Capability
Turn a script into an operable tool with documented arguments, exit behavior, and help.

A CLI is useful for scheduled jobs, local operations, CI tasks, and n8n subprocess/service boundaries.

Use `argparse` (or a later approved alternative) to define:
- required/optional arguments;
- defaults;
- choices/types;
- help text.

## Practice
Build:
`python normalize_orders.py --input raw.csv --output clean.csv --strict`

Requirements:
- `--help` works;
- invalid path returns nonzero exit;
- output is not silently overwritten unless explicitly allowed;
- summary counts are printed/logged.

## Mastery
Another person can discover how to run the tool without reading its source.
