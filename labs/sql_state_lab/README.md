# SQL State Lab

Design persistent state for an event-processing automation.

Required properties:

- unique event ID,
- status (`received`, `processing`, `completed`, `failed`),
- attempt count,
- timestamps,
- last error,
- business result reference.

Use `schema.sql` as the starting contract. Test duplicate inserts, retry updates, and a transaction that changes state plus writes an output record atomically.
