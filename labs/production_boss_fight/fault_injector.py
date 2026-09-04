from __future__ import annotations

import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def send(raw: bytes) -> tuple[int, str]:
    request = Request("http://127.0.0.1:8088/event", data=raw, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=2) as response:
            return response.status, response.read().decode()
    except HTTPError as error:
        return error.code, error.read().decode()


cases = [
    json.dumps({"event_id": "evt-1", "value": 10}).encode(),
    json.dumps({"event_id": "evt-1", "value": 10}).encode(),
    b"{not-json",
    json.dumps({"value": 99}).encode(),
]

for case in cases:
    print(send(case))
