from __future__ import annotations

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def deliver(url: str, event: dict) -> tuple[int, str]:
    body = json.dumps(event).encode("utf-8")
    request = Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "X-Lab-Delivery": event["event_id"]},
        method="POST",
    )
    try:
        with urlopen(request, timeout=3) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        return error.code, error.read().decode("utf-8", errors="replace")
    except URLError as error:
        return 0, str(error.reason)


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:9000/webhook"
    events = [
        {"event_id": "evt-100", "type": "customer.updated", "value": 10},
        {"event_id": "evt-100", "type": "customer.updated", "value": 10},
        {"event_id": "evt-101", "type": "customer.updated", "value": 20},
    ]
    print(f"Delivering to {url}")
    for event in events:
        status, response = deliver(url, event)
        print(event["event_id"], status, response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
