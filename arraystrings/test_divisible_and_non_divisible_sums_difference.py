import unittest
from .divisible_and_non_divisible_sums_difference import Solution


class TestDivisibleAndNonDivisibleSumsDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_small_numbers(self):
        self.assertEqual(self.solution.differenceOfSums(10, 3), 19)
        self.assertEqual(self.solution.differenceOfSums(5, 2), 3)
        self.assertEqual(self.solution.differenceOfSums(4, 2), -2)

    def test_edge_cases(self):
        self.assertEqual(self.solution.differenceOfSums(1, 1), -1)
        self.assertEqual(self.solution.differenceOfSums(1, 2), 1)
        self.assertEqual(self.solution.differenceOfSums(2, 1), -3)

    def test_equal_numbers(self):
        self.assertEqual(self.solution.differenceOfSums(3, 3), 0)
        self.assertEqual(self.solution.differenceOfSums(4, 4), 2)
        self.assertEqual(self.solution.differenceOfSums(5, 5), 5)

    def test_larger_numbers(self):
        self.assertEqual(self.solution.differenceOfSums(15, 4), 72)
        self.assertEqual(self.solution.differenceOfSums(20, 5), 110)
        self.assertEqual(self.solution.differenceOfSums(25, 6), 205)

    def test_prime_numbers(self):
        self.assertEqual(self.solution.differenceOfSums(7, 2), 4)
        self.assertEqual(self.solution.differenceOfSums(11, 3), 30)
        self.assertEqual(self.solution.differenceOfSums(13, 5), 61)


if __name__ == "__main__":
    unittest.main()
