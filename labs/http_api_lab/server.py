from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


def simulated_response(path: str, query: dict[str, list[str]]) -> tuple[int, dict[str, str], dict]:
    if path == "/ok":
        return 200, {}, {"ok": True}
    if path == "/unauthorized":
        return 401, {}, {"error": "missing_or_invalid_token"}
    if path == "/forbidden":
        return 403, {}, {"error": "insufficient_permission"}
    if path == "/rate-limit":
        attempt = int(query.get("attempt", ["1"])[0])
        if attempt < 3:
            return 429, {"Retry-After": "1"}, {"error": "rate_limited", "attempt": attempt}
        return 200, {}, {"ok": True, "attempt": attempt}
    if path == "/unstable":
        attempt = int(query.get("attempt", ["1"])[0])
        if attempt == 1:
            return 503, {}, {"error": "temporary_unavailable"}
        return 200, {}, {"ok": True, "attempt": attempt}
    if path == "/items":
        cursor = int(query.get("cursor", ["0"])[0])
        page_size = 2
        items = ["alpha", "beta", "gamma", "delta", "epsilon"]
        page = items[cursor : cursor + page_size]
        next_cursor = cursor + page_size if cursor + page_size < len(items) else None
        return 200, {}, {"items": page, "next_cursor": next_cursor}
    return 404, {}, {"error": "not_found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        status, headers, body = simulated_response(parsed.path, parse_qs(parsed.query))
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print("Automation API lab listening on http://127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
