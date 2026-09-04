import unittest
from pathlib import Path

from evaluator import score


class EvalTests(unittest.TestCase):
    def test_baseline_contract(self) -> None:
        correct, total = score(Path(__file__).with_name("cases.json"))
        self.assertEqual((correct, total), (4, 4))


if __name__ == "__main__":
    unittest.main()
