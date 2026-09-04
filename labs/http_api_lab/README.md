# HTTP/API Reliability Lab

`server.py` is a local API simulator. It can produce success, auth failures, rate limits, transient failures, pagination, malformed input, and duplicate webhook deliveries.

Start it:

```bash
python server.py
```

Then build a client that:

- distinguishes transport errors from HTTP errors,
- handles 401/403 differently,
- honors `Retry-After`,
- retries only appropriate failures,
- paginates until completion,
- deduplicates webhook event IDs.

Use `test_server.py` to verify the simulator itself. Your client is the learner artifact.
