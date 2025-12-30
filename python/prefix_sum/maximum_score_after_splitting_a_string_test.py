import unittest

from .maximum_score_after_splitting_a_string import Solution


class TestMaxScore(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test basic case with mixed 0s and 1s"""
        s = "011101"
        self.assertEqual(self.solution.maxScore(s), 5)
        # Split after index 0: Left="0" (1 zero), Right="11101" (4 ones)

    def test_alternating_bits(self):
        """Test string with alternating 0s and 1s"""
        s = "01010"
        self.assertEqual(self.solution.maxScore(s), 3)
        # Split after index 1: Left="0" (1 zero), Right="1010" (2 ones)

    def test_all_zeros(self):
        """Test string with all zeros except last required 1"""
        s = "00001"
        self.assertEqual(self.solution.maxScore(s), 5)
        # Split after index 3: Left="0000" (4 zeros), Right="1" (1 one)

    def test_all_ones(self):
        """Test string with all ones except first required 0"""
        s = "01111"
        self.assertEqual(self.solution.maxScore(s), 5)
        # Split after index 0: Left="0" (1 zero), Right="1111" (4 ones)

    def test_minimum_length(self):
        """Test minimum possible length string (2 characters)"""
        s = "01"
        self.assertEqual(self.solution.maxScore(s), 2)
        # Only possible split: Left="0" (1 zero), Right="1" (1 one)

        s = "10"
        self.assertEqual(self.solution.maxScore(s), 0)
        # Only possible split has no zeros on left and no ones on right

    def test_balanced_distribution(self):
        """Test with equal numbers of 0s and 1s"""
        s = "001111"
        self.assertEqual(self.solution.maxScore(s), 6)
        # Split after index 1: Left="00" (2 zeros), Right="1111" (4 ones)

    def test_optimal_split_end(self):
        """Test when optimal split is near the end"""
        s = "1111110"
        self.assertEqual(self.solution.maxScore(s), 5)
        # Split after index 5: Left="111111" (0 zeros), Right="0" (5 ones)

    def test_optimal_split_start(self):
        """Test when optimal split is near the start"""
        s = "0111111"
        self.assertEqual(self.solution.maxScore(s), 7)
        # Split after index 0: Left="0" (1 zero), Right="111111" (6 ones)

    def test_long_string(self):
        """Test with a longer string"""
        s = "00111100111100"
        self.assertEqual(self.solution.maxScore(s), 10)
        # Tests handling of longer patterns


if __name__ == "__main__":
    unittest.main()
