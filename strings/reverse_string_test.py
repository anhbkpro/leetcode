import unittest
from .reverse_string import SolutionOnSpace, SolutionO1Space


class BaseTestReverseString:
    """Base test class with common test cases"""
    def setUp(self):
        self.solution = self.SolutionClass()

    def test_basic_string(self):
        """Test with basic string"""
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_empty_string(self):
        """Test with empty string"""
        s = []
        self.solution.reverseString(s)
        self.assertEqual(s, [])

    def test_single_character(self):
        """Test with single character"""
        s = ["a"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["a"])

    def test_palindrome(self):
        """Test with palindrome"""
        s = ["r", "a", "d", "a", "r"]
        original = s.copy()
        self.solution.reverseString(s)
        self.assertEqual(s, original)

    def test_all_same_characters(self):
        """Test with all same characters"""
        s = ["a", "a", "a"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["a", "a", "a"])

    def test_special_characters(self):
        """Test with special characters"""
        s = ["!", "@", "#", "$", "%"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["%", "$", "#", "@", "!"])

    def test_numbers_as_strings(self):
        """Test with numbers as strings"""
        s = ["1", "2", "3", "4", "5"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["5", "4", "3", "2", "1"])

    def test_mixed_characters(self):
        """Test with mixed characters"""
        s = ["a", "1", "@", "b", "2"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["2", "b", "@", "1", "a"])

    def test_long_string(self):
        """Test with a long string to verify performance"""
        s = list("abcdefghijklmnopqrstuvwxyz")
        expected = list("zyxwvutsrqponmlkjihgfedcba")
        self.solution.reverseString(s)
        self.assertEqual(s, expected)


class TestReverseStringRecursive(BaseTestReverseString, unittest.TestCase):
    """Test cases for the recursive solution with O(N) space"""
    SolutionClass = SolutionOnSpace


class TestReverseStringIterative(BaseTestReverseString, unittest.TestCase):
    """Test cases for the iterative solution with O(1) space"""
    SolutionClass = SolutionO1Space


if __name__ == "__main__":
    unittest.main()
