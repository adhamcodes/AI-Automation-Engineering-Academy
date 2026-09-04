import unittest

from service import normalize_customer


class NormalizeTests(unittest.TestCase):
    def test_normalizes_email_and_name(self) -> None:
        result = normalize_customer({"name": "  Ada  ", "email": "ADA@EXAMPLE.COM"})
        self.assertEqual(result["name"], "Ada")
        self.assertEqual(result["email"], "ada@example.com")

    def test_rejects_bad_email(self) -> None:
        with self.assertRaises(ValueError):
            normalize_customer({"name": "Ada", "email": "not-an-email"})


if __name__ == "__main__":
    unittest.main()
