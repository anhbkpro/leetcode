import unittest
from .cutting_ribbons import Solution


class TestRibbonCutting(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_length_basic(self):
        """Test basic cases for maxLength method"""
        # Test case from example
        ribbons = [9, 7, 5]
        k = 3
        self.assertEqual(self.solution.maxLength(ribbons, k), 5)

    def test_max_length_equal_ribbons(self):
        """Test when all ribbons are equal length"""
        ribbons = [5, 5, 5, 5]
        k = 8
        self.assertEqual(self.solution.maxLength(ribbons, k), 2)
        # Each ribbon can be cut into 2 pieces of length 2

    def test_max_length_single_ribbon(self):
        """Test with a single ribbon"""
        ribbons = [10]
        k = 5
        self.assertEqual(self.solution.maxLength(ribbons, k), 2)
        # One ribbon of length 10 can be cut into 5 pieces of length 2

    def test_max_length_impossible(self):
        """Test when it's impossible to cut enough pieces"""
        ribbons = [3, 2, 1]
        k = 10
        self.assertEqual(self.solution.maxLength(ribbons, k), 0)
        # Can't get 10 pieces from these ribbons

    def test_max_length_exact_division(self):
        """Test when ribbons can be divided exactly"""
        ribbons = [6, 6, 6]
        k = 9
        self.assertEqual(self.solution.maxLength(ribbons, k), 2)
        # Each ribbon can be cut into exactly 3 pieces of length 2

    def test_max_length_different_lengths(self):
        """Test with ribbons of very different lengths"""
        ribbons = [1, 2, 3, 4, 9]
        k = 5
        self.assertEqual(self.solution.maxLength(ribbons, k), 3)
        # Can get 5 pieces of length 2 (0+1+1+2+4 pieces from each ribbon)

    def test_max_length_large_numbers(self):
        """Test with large ribbon lengths"""
        ribbons = [100, 200, 300]
        k = 10
        self.assertEqual(self.solution.maxLength(ribbons, k), 50)
        # Can cut each ribbon into multiple pieces of length 50

    def test_max_length_minimum_k(self):
        """Test with k=1"""
        ribbons = [5, 7, 9]
        k = 1
        self.assertEqual(self.solution.maxLength(ribbons, k), 9)
        # Can get one piece of length 9 from the longest ribbon

    def test_edge_cases(self):
        """Test edge cases"""

        # Single ribbon, k=1
        self.assertEqual(self.solution.maxLength([5], 1), 5)

        # All ribbons length 1
        self.assertEqual(self.solution.maxLength([1, 1, 1], 3), 1)


if __name__ == "__main__":
    unittest.main()
