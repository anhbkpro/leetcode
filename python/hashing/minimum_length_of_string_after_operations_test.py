import unittest

from .minimum_length_of_string_after_operations import Solution


class TestMinimumLength(unittest.TestCase):
    def setUp(self):
        """Initialize the Solution class before each test"""
        self.solution = Solution()

    def test_example_cases(self):
        """Test the examples given in the problem description"""
        self.assertEqual(self.solution.minimumLength("abaacbcbb"), 5)
        self.assertEqual(self.solution.minimumLength("aa"), 2)

    def test_single_character(self):
        """Test strings with single character"""
        self.assertEqual(self.solution.minimumLength("a"), 1)

    def test_two_characters(self):
        """Test strings with two characters"""
        self.assertEqual(self.solution.minimumLength("ab"), 2)
        self.assertEqual(self.solution.minimumLength("aa"), 2)

    def test_same_characters(self):
        """Test strings with all same characters"""
        self.assertEqual(self.solution.minimumLength("aaa"), 1)
        self.assertEqual(self.solution.minimumLength("aaaa"), 2)
        self.assertEqual(self.solution.minimumLength("aaaaa"), 1)

    def test_alternating_characters(self):
        """Test strings with alternating characters"""
        self.assertEqual(self.solution.minimumLength("ababab"), 2)
        self.assertEqual(self.solution.minimumLength("abcabc"), 6)

    def test_palindromes(self):
        """Test palindromic strings"""
        self.assertEqual(self.solution.minimumLength("aba"), 3)
        self.assertEqual(self.solution.minimumLength("abba"), 4)
        self.assertEqual(self.solution.minimumLength("abcba"), 5)

    def test_complex_cases(self):
        """Test more complex string patterns"""
        self.assertEqual(self.solution.minimumLength("aabbaabb"), 4)
        self.assertEqual(self.solution.minimumLength("abbbbba"), 3)
        self.assertEqual(self.solution.minimumLength("abcdefg"), 7)
        self.assertEqual(self.solution.minimumLength("cabaabac"), 6)

    def test_edge_cases(self):
        """Test edge cases with minimum and maximum lengths"""
        # Minimum length string
        self.assertEqual(self.solution.minimumLength("a"), 1)
        # Long string with same character
        self.assertEqual(self.solution.minimumLength("a" * 200000), 2)
        # Long string that can't be reduced
        self.assertEqual(self.solution.minimumLength("ab" * 100000), 4)

    def test_multiple_deletions(self):
        """Test cases requiring multiple deletion operations"""
        self.assertEqual(self.solution.minimumLength("aaaabaaa"), 2)
        self.assertEqual(self.solution.minimumLength("aaabbaaa"), 4)
        self.assertEqual(self.solution.minimumLength("abababab"), 4)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
