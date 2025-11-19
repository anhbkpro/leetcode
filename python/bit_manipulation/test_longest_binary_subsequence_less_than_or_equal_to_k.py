import unittest

from .longest_binary_subsequence_less_than_or_equal_to_k import Solution


class TestLongestSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: s = "1001010", k = 5"""
        s = "1001010"
        k = 5
        expected = 5
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        """Test Example 2: s = "00101001", k = 1"""
        s = "00101001"
        k = 1
        expected = 6
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_zeros(self):
        """Test case with all zeros"""
        s = "0000"
        k = 5
        expected = 4  # All zeros can be included
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_ones_small_k(self):
        """Test case with all ones but small k"""
        s = "1111"
        k = 2
        expected = 1  # Only first 1 can be included (1 = 1 <= 2)
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_mixed_bits_large_k(self):
        """Test case with mixed bits and large k"""
        s = "101010"
        k = 50
        expected = 6  # All bits can be included
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_bit(self):
        """Test case with single bit"""
        s = "1"
        k = 1
        expected = 1
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_zero(self):
        """Test case with single zero"""
        s = "0"
        k = 5
        expected = 1
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_k_equals_zero(self):
        """Test case where k = 0"""
        s = "1001"
        k = 0
        expected = 2  # Only zeros can be included
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_large_binary_string(self):
        """Test case with larger binary string"""
        s = "110010101"
        k = 10
        expected = 6  # Should include most bits but not exceed k
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_leading_zeros_important(self):
        """Test case where leading zeros are important"""
        s = "001100"
        k = 3
        expected = 4  # Should include leading zeros and some ones
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_maximum_k(self):
        """Test case with maximum k value"""
        s = "1010101010"
        k = 10**9
        expected = 10  # All bits can be included
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_minimum_length_string(self):
        """Test case with minimum length string"""
        s = "1"
        k = 1
        expected = 1
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_complex_case(self):
        """Test a more complex case"""
        s = "101101"
        k = 6
        expected = 4  # Should include most bits but not exceed k
        result = self.solution.longestSubsequence(s, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
