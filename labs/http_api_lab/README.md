# HTTP/API Reliability Lab

`server.py` is a local API simulator. It produces success, auth failures, rate limits, transient failures, pagination, and explicit error responses.

Start it:

```bash
python server.py
```

Then build a client that:

- distinguishes transport errors from HTTP errors,
- handles 401/403 differently,
- honors `Retry-After`,
- retries only appropriate failures,
- paginates until completion.

## Duplicate webhook exercise

Build a small local webhook receiver that accepts JSON POST requests and records business effects by `event_id`. Then, in another terminal, run:

```bash
python webhook_sender.py http://127.0.0.1:9000/webhook
```

The sender deliberately delivers `evt-100` twice and then a distinct `evt-101`. Your receiver must acknowledge both deliveries safely while applying the business effect for `evt-100` only once.

Use `test_server.py` to verify the API simulator itself. Your client and webhook receiver are learner artifacts.
