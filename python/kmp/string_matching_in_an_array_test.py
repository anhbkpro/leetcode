import unittest

from .string_matching_in_an_array import Solution


class TestStringMatching(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from Example 1: ["mass","as","hero","superhero"]"""
        words = ["mass", "as", "hero", "superhero"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["as", "hero"]))

    def test_example_2(self):
        """Test case from Example 2: ["leetcode","et","code"]"""
        words = ["leetcode", "et", "code"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["et", "code"]))

    def test_example_3(self):
        """Test case from Example 3: ["blue","green","bu"]"""
        words = ["blue", "green", "bu"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, [])

    def test_single_word(self):
        """Test array with a single word"""
        words = ["hello"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, [])

    def test_overlapping_substrings(self):
        """Test words with overlapping substring patterns"""
        words = ["ababab", "aba", "bab"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["aba", "bab"]))

    def test_repeated_characters(self):
        """Test strings with repeated characters"""
        words = ["aaa", "aa", "a"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["a", "aa"]))

    def test_boundary_conditions(self):
        """Test boundary conditions with max length strings"""
        words = ["a" * 30, "a" * 15]  # Max length is 30
        result = self.solution.stringMatching(words)
        self.assertEqual(result, ["a" * 15])

    def test_compute_lps_array(self):
        """Test the LPS array computation"""
        test_cases = [
            ("AAAA", [0, 1, 2, 3]),
            ("ABCDE", [0, 0, 0, 0, 0]),
            ("AABAACAABAA", [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]),
        ]
        for pattern, expected in test_cases:
            result = self.solution._compute_lps_array(pattern)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
