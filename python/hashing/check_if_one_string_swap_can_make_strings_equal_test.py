import unittest
from .check_if_one_string_swap_can_make_strings_equal import (
    Solution,
    SolutionFrequencyMapCheckDifferences,
    SolutionOnlyCheckDifferences,
)


class BaseTestAreAlmostEqual:
    """Base test class containing all test cases"""

    def setUp(self):
        self.solution = self.solution_class()

    def test_strings_are_equal(self):
        """Test when strings are already equal"""
        self.assertTrue(self.solution.areAlmostEqual("hello", "hello"))

    def test_strings_can_be_made_equal_with_one_swap(self):
        """Test when strings can be made equal with one swap"""
        self.assertTrue(self.solution.areAlmostEqual("bank", "kanb"))

    def test_strings_with_different_characters(self):
        """Test when strings have different characters"""
        self.assertFalse(self.solution.areAlmostEqual("hello", "world"))

    def test_strings_with_different_lengths(self):
        """Test when strings have different lengths"""
        self.assertFalse(self.solution.areAlmostEqual("abc", "abcd"))

    def test_strings_requiring_multiple_swaps(self):
        """Test when strings would require more than one swap"""
        self.assertFalse(self.solution.areAlmostEqual("abcd", "dcba"))

    def test_empty_strings(self):
        """Test with empty strings"""
        self.assertTrue(self.solution.areAlmostEqual("", ""))

    def test_single_character_strings(self):
        """Test with single character strings"""
        self.assertTrue(self.solution.areAlmostEqual("a", "a"))
        self.assertFalse(self.solution.areAlmostEqual("a", "b"))

    def test_strings_with_repeated_characters(self):
        """Test strings with repeated characters"""
        self.assertTrue(self.solution.areAlmostEqual("aabc", "abac"))
        self.assertFalse(self.solution.areAlmostEqual("aabc", "abcc"))


class TestSolutionCounter(BaseTestAreAlmostEqual, unittest.TestCase):
    """Test cases for the Counter-based solution"""

    solution_class = Solution


class TestSolutionFrequencyMap(BaseTestAreAlmostEqual, unittest.TestCase):
    """Test cases for the frequency map solution"""

    solution_class = SolutionFrequencyMapCheckDifferences


class TestSolutionDifferences(BaseTestAreAlmostEqual, unittest.TestCase):
    """Test cases for the differences-only solution"""

    solution_class = SolutionOnlyCheckDifferences


if __name__ == "__main__":
    unittest.main()
