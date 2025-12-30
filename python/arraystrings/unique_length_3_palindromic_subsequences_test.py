import unittest

from .unique_length_3_palindromic_subsequences import Solution


class TestPalindromicSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Test the example case from the problem description"""
        self.assertEqual(self.solution.countPalindromicSubsequence("aabca"), 3)

    def test_all_same_letters(self):
        """Test string with all same letters - should return 1"""
        self.assertEqual(self.solution.countPalindromicSubsequence("aaaa"), 1)

    def test_no_palindromes(self):
        """Test string that contains no palindromic subsequences of length 3"""
        self.assertEqual(self.solution.countPalindromicSubsequence("abc"), 0)

    def test_minimum_length(self):
        """Test strings of length less than 3"""
        self.assertEqual(self.solution.countPalindromicSubsequence("aa"), 0)
        self.assertEqual(self.solution.countPalindromicSubsequence("a"), 0)
        self.assertEqual(self.solution.countPalindromicSubsequence(""), 0)

    def test_multiple_occurrences(self):
        """Test string with multiple ways to form same palindrome"""
        # "bbbb" can form "bbb" in multiple ways but should count only once
        self.assertEqual(self.solution.countPalindromicSubsequence("bbbb"), 1)

    def test_all_unique_letters(self):
        """Test string with all unique letters"""
        self.assertEqual(self.solution.countPalindromicSubsequence("abcde"), 0)

    def test_complex_case(self):
        """Test more complex string with multiple palindromic subsequences"""
        # Should find: "aba", "aca", "ada", "aaa"
        self.assertEqual(self.solution.countPalindromicSubsequence("abcaada"), 4)

    def test_repeated_patterns(self):
        """Test string with repeated patterns"""
        # Should find: "aaa", "aba", "aca"
        self.assertEqual(self.solution.countPalindromicSubsequence("aabcaa"), 3)

    def test_special_characters(self):
        """Test string with special characters and spaces"""
        self.assertEqual(self.solution.countPalindromicSubsequence("a!a"), 1)
        self.assertEqual(self.solution.countPalindromicSubsequence("a a"), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
