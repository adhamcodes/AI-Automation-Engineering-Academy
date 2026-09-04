from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

processed: set[str] = set()


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: dict) -> None:
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, {"status": "ok", "processed": len(processed)})
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/event":
            self._send(404, {"error": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(length))
        except (ValueError, json.JSONDecodeError):
            self._send(400, {"error": "invalid_json"})
            return
        event_id = body.get("event_id")
        if not event_id:
            self._send(400, {"error": "event_id_required"})
            return
        if event_id in processed:
            self._send(200, {"status": "duplicate_ignored", "event_id": event_id})
            return
        processed.add(event_id)
        self._send(201, {"status": "processed", "event_id": event_id})

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print("Boss-fight service listening on http://127.0.0.1:8088")
    ThreadingHTTPServer(("127.0.0.1", 8088), Handler).serve_forever()
