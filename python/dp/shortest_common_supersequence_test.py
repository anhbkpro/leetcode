import unittest

from dp.shortest_common_supersequence import (
    SolutionBacktrackingTLE,
    SolutionBottomUpDynamicProgramming,
    SolutionMemoizationTLE,
    SolutionMostOptimalSpaceOptimizedDynamicProgramming,
)


class TestShortestCommonSupersequence(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionBacktrackingTLE(),
            SolutionMemoizationTLE(),
            SolutionBottomUpDynamicProgramming(),
            SolutionMostOptimalSpaceOptimizedDynamicProgramming(),
        ]

    def test_empty_strings(self):
        for solution in self.solutions:
            self.assertEqual(solution.shortestCommonSupersequence("", ""), "")

    def test_one_empty_string(self):
        for solution in self.solutions:
            self.assertEqual(solution.shortestCommonSupersequence("", "abc"), "abc")
            self.assertEqual(solution.shortestCommonSupersequence("xyz", ""), "xyz")

    def test_same_strings(self):
        for solution in self.solutions:
            self.assertEqual(solution.shortestCommonSupersequence("abc", "abc"), "abc")

    def test_no_common_characters(self):
        for solution in self.solutions:
            result = solution.shortestCommonSupersequence("abc", "def")
            # Both "abcdef" and "defabc" are valid results
            self.assertEqual(len(result), 6)
            self.assertTrue(
                all(c in result for c in "abc") and all(c in result for c in "def")
            )

    def test_partial_overlap(self):
        for solution in self.solutions:
            result = solution.shortestCommonSupersequence("abac", "cab")
            # "cabac" is one valid result
            self.assertEqual(len(result), 5)
            self.assertTrue(
                all(c in result for c in "abac") and all(c in result for c in "cab")
            )

    def test_leetcode_example(self):
        for solution in self.solutions:
            result = solution.shortestCommonSupersequence("abac", "cab")
            self.assertEqual(len(result), 5)
            # Verify that both input strings are subsequences of the result
            self.assertTrue(self.is_subsequence("abac", result))
            self.assertTrue(self.is_subsequence("cab", result))

    def test_longer_strings(self):
        for solution in self.solutions:
            result = solution.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaaa")
            self.assertEqual(len(result), 9)
            self.assertEqual(result, "aaaaaaaaa")

    def is_subsequence(self, s: str, t: str) -> bool:
        """Helper method to check if s is a subsequence of t."""
        if not s:
            return True
        if not t:
            return False

        s_idx = 0
        for char in t:
            if char == s[s_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
