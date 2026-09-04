from __future__ import annotations

import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen

from server import Handler, simulated_response


class SimulatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        host, port = cls.server.server_address
        cls.base_url = f"http://{host}:{port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get(self, path: str) -> tuple[int, dict[str, str], dict]:
        try:
            with urlopen(self.base_url + path, timeout=2) as response:
                return response.status, dict(response.headers.items()), json.loads(response.read())
        except HTTPError as error:
            return error.code, dict(error.headers.items()), json.loads(error.read())

    def test_pure_rate_limit_contract(self) -> None:
        self.assertEqual(simulated_response("/rate-limit", {"attempt": ["1"]})[0], 429)
        status, _, body = simulated_response("/rate-limit", {"attempt": ["3"]})
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])

    def test_real_http_auth_statuses(self) -> None:
        self.assertEqual(self.get("/unauthorized")[0], 401)
        self.assertEqual(self.get("/forbidden")[0], 403)
        self.assertEqual(self.get("/does-not-exist")[0], 404)

    def test_real_http_rate_limit_exposes_retry_after(self) -> None:
        status, headers, body = self.get("/rate-limit?attempt=1")
        self.assertEqual(status, 429)
        self.assertEqual(headers.get("Retry-After"), "1")
        self.assertEqual(body["error"], "rate_limited")
        self.assertEqual(self.get("/rate-limit?attempt=3")[0], 200)

    def test_real_http_pagination_finishes(self) -> None:
        seen: list[str] = []
        cursor = 0
        while True:
            status, _, body = self.get(f"/items?cursor={cursor}")
            self.assertEqual(status, 200)
            seen.extend(body["items"])
            if body["next_cursor"] is None:
                break
            cursor = body["next_cursor"]
        self.assertEqual(seen, ["alpha", "beta", "gamma", "delta", "epsilon"])


if __name__ == "__main__":
    unittest.main()
