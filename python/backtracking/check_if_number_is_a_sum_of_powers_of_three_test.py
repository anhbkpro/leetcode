import unittest

from backtracking.check_if_number_is_a_sum_of_powers_of_three import Solution


class TestCheckPowersOfThree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_numbers(self):
        # Test cases where numbers can be expressed as sum of powers of 3
        self.assertTrue(self.solution.checkPowersOfThree(12))  # 3^1 + 3^2
        self.assertTrue(self.solution.checkPowersOfThree(91))  # 3^0 + 3^2 + 3^4
        self.assertTrue(self.solution.checkPowersOfThree(13))  # 3^0 + 3^1 + 3^2
        self.assertTrue(self.solution.checkPowersOfThree(1))  # 3^0

    def test_invalid_numbers(self):
        # Test cases where numbers cannot be expressed as sum of powers of 3
        self.assertFalse(self.solution.checkPowersOfThree(2))  # Cannot be expressed
        self.assertFalse(self.solution.checkPowersOfThree(5))  # Cannot be expressed
        self.assertFalse(self.solution.checkPowersOfThree(7))  # Cannot be expressed

    def test_edge_cases(self):
        # Test edge cases
        self.assertTrue(self.solution.checkPowersOfThree(0))  # Empty sum
        self.assertTrue(self.solution.checkPowersOfThree(1))  # 3^0
        self.assertFalse(self.solution.checkPowersOfThree(-1))  # Negative number


if __name__ == "__main__":
    unittest.main()
