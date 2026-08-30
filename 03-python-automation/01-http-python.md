# Module 3.1 — HTTP Clients in Python

## Capability
Call APIs from Python while explicitly handling timeout, status, JSON decoding, and network failures.

A useful client function should not be `requests.get(url).json()` and hope for the best.

Core pattern:
```python
response = requests.get(url, params=params, headers=headers, timeout=10)
response.raise_for_status()
data = response.json()
```

Important distinctions:
- network exception vs HTTP error response;
- successful JSON decoding vs successful HTTP operation;
- connect/read timeout vs "total job deadline";
- authentication/configuration vs business payload.

Requests documentation explicitly recommends using timeouts in nearly all production code; without one, a request may wait indefinitely.

## Practice
Write `fetch_customer(customer_id)` with:
- base URL from config;
- timeout;
- explicit handling for 404 vs other errors;
- safe logging without token exposure;
- return type/shape documented.

## Mastery
You can explain every failure path and never rely on JSON parsing as proof of success.
