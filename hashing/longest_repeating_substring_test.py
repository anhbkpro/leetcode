import unittest
from .longest_repeating_substring import Solution


class TestLongestRepeatingSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test example case with multiple repeating substrings"""
        s = "abbaba"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 2)  # "ab" repeats

    def test_example_2(self):
        """Test example case with longer repeating substring"""
        s = "aabcaabdaab"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 3)  # "aab" repeats

    def test_no_repeating_substring(self):
        """Test when there is no repeating substring"""
        s = "abcd"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 0)

    def test_all_same_characters(self):
        """Test when all characters are the same"""
        s = "aaaa"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 3)  # "aaa" repeats

    def test_overlapping_substrings(self):
        """Test with overlapping repeating substrings"""
        s = "aabaabaa"
        self.assertEqual(
            self.solution.longestRepeatingSubstring(s), 5
        )  # "aabaa" repeats

    def test_empty_string(self):
        """Test with empty string"""
        s = ""
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 0)

    def test_single_character(self):
        """Test with single character"""
        s = "a"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 0)

    def test_two_characters(self):
        """Test with two characters"""
        s = "aa"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 1)  # "a" repeats

    def test_multiple_possible_substrings(self):
        """Test with multiple possible repeating substrings of different lengths"""
        s = "ababab"
        self.assertEqual(
            self.solution.longestRepeatingSubstring(s), 4
        )  # "abab" repeats

    def test_case_sensitive(self):
        """Test that the search is case-sensitive"""
        s = "aAaA"
        self.assertEqual(self.solution.longestRepeatingSubstring(s), 2)  # "aA" repeats


if __name__ == "__main__":
    unittest.main()
