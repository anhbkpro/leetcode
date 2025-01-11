import unittest
from .construct_k_palindrome_strings import Solution


class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        # Example 1
        self.assertTrue(self.solution.canConstruct("annabelle", 2))
        # Example 2
        self.assertFalse(self.solution.canConstruct("leetcode", 3))
        # Example 3
        self.assertTrue(self.solution.canConstruct("true", 4))

    def test_edge_cases(self):
        # Single character
        self.assertTrue(self.solution.canConstruct("a", 1))
        # k equals string length
        self.assertTrue(self.solution.canConstruct("abcd", 4))
        # k greater than string length
        self.assertFalse(self.solution.canConstruct("abc", 4))

    def test_all_same_characters(self):
        # All same characters can be split into any number <= length
        self.assertTrue(self.solution.canConstruct("aaaa", 2))
        self.assertTrue(self.solution.canConstruct("aaaa", 4))
        self.assertFalse(self.solution.canConstruct("aaaa", 5))

    def test_palindrome_patterns(self):
        # Already palindrome
        self.assertTrue(self.solution.canConstruct("racecar", 1))
        # Can be split into two palindromes
        self.assertTrue(self.solution.canConstruct("aabb", 2))
        # Cannot be split into required palindromes
        self.assertFalse(self.solution.canConstruct("abc", 2))

    def test_odd_count_scenarios(self):
        # Multiple odd count characters
        self.assertTrue(self.solution.canConstruct("aabbc", 3))
        self.assertTrue(self.solution.canConstruct("aabbc", 2))
        # All odd count characters
        self.assertTrue(self.solution.canConstruct("abcde", 5))
        self.assertFalse(self.solution.canConstruct("abcde", 4))

    def test_constraint_boundaries(self):
        # Minimum length and k
        self.assertTrue(self.solution.canConstruct("a", 1))
        # Length equals k
        self.assertTrue(self.solution.canConstruct("abcde", 5))
        # k is 1 but string can form palindrome
        self.assertTrue(self.solution.canConstruct("aa", 1))


if __name__ == "__main__":
    unittest.main()
