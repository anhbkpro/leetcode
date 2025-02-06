import unittest
from .check_if_one_string_swap_can_make_strings_equal import Solution


class TestAreAlmostEqual(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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


if __name__ == '__main__':
    unittest.main()
