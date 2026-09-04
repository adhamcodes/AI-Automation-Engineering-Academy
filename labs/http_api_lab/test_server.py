import unittest

from server import simulated_response


class SimulatorTests(unittest.TestCase):
    def test_rate_limit_recovers_on_third_attempt(self) -> None:
        self.assertEqual(simulated_response("/rate-limit", {"attempt": ["1"]})[0], 429)
        status, _, body = simulated_response("/rate-limit", {"attempt": ["3"]})
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])

    def test_pagination_finishes(self) -> None:
        seen = []
        cursor = 0
        while True:
            status, _, body = simulated_response("/items", {"cursor": [str(cursor)]})
            self.assertEqual(status, 200)
            seen.extend(body["items"])
            if body["next_cursor"] is None:
                break
            cursor = body["next_cursor"]
        self.assertEqual(seen, ["alpha", "beta", "gamma", "delta", "epsilon"])


if __name__ == "__main__":
    unittest.main()
