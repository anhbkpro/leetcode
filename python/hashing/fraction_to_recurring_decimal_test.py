import unittest
from hashing.fraction_to_recurring_decimal import Solution


class TestFractionToDecimal(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 2), "0.5")

    def test_example2(self):
        self.assertEqual(self.sol.fractionToDecimal(2, 1), "2")

    def test_example3(self):
        self.assertEqual(self.sol.fractionToDecimal(4, 333), "0.(012)")

    def test_negative(self):
        self.assertEqual(self.sol.fractionToDecimal(-1, 2), "-0.5")
        self.assertEqual(self.sol.fractionToDecimal(1, -2), "-0.5")
        self.assertEqual(self.sol.fractionToDecimal(-1, -2), "0.5")

    def test_zero(self):
        self.assertEqual(self.sol.fractionToDecimal(0, 5), "0")

    def test_repeating(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 3), "0.(3)")
        self.assertEqual(self.sol.fractionToDecimal(2, 3), "0.(6)")
        self.assertEqual(self.sol.fractionToDecimal(1, 6), "0.1(6)")

    def test_no_fraction(self):
        self.assertEqual(self.sol.fractionToDecimal(10, 2), "5")


if __name__ == "__main__":
    unittest.main()
