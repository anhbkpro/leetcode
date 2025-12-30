import unittest

from .count_vowel_strings_in_ranges import Solution


class TestVowelStrings(unittest.TestCase):
    def setUp(self):
        """Initialize the Solution class before each test."""
        self.solution = Solution()

    def test_example_cases(self):
        """Test the example cases provided in the problem description."""
        # Test case 1
        words1 = ["aba", "bcb", "ece", "aa", "e"]
        queries1 = [[0, 2], [1, 4], [1, 1]]
        expected1 = [2, 3, 0]
        self.assertEqual(
            self.solution.vowelStrings(words1, queries1),
            expected1,
            "Failed example test case 1",
        )

        # Test case 2
        words2 = ["a", "e", "i"]
        queries2 = [[0, 2], [0, 1], [2, 2]]
        expected2 = [3, 2, 1]
        self.assertEqual(
            self.solution.vowelStrings(words2, queries2),
            expected2,
            "Failed example test case 2",
        )

    def test_edge_cases(self):
        """Test edge cases with minimal inputs and boundary conditions."""
        # Single word, single query
        self.assertEqual(
            self.solution.vowelStrings(["a"], [[0, 0]]), [1], "Failed single word test"
        )

        # Empty word list
        self.assertEqual(
            self.solution.vowelStrings([], []), [], "Failed empty input test"
        )

        # No valid vowel strings
        self.assertEqual(
            self.solution.vowelStrings(["bc", "cd", "df"], [[0, 2]]),
            [0],
            "Failed no vowel strings test",
        )

    def test_all_vowel_strings(self):
        """Test cases where all strings start and end with vowels."""
        words = ["aa", "ee", "ii", "oo", "uu"]
        queries = [
            [0, 4],  # All strings
            [1, 3],  # Middle subset
            [0, 0],  # First string
            [4, 4],  # Last string
        ]
        expected = [5, 3, 1, 1]
        self.assertEqual(
            self.solution.vowelStrings(words, queries),
            expected,
            "Failed all vowel strings test",
        )

    def test_mixed_cases(self):
        """Test with a mix of valid and invalid strings."""
        words = ["apple", "banana", "ice", "orange", "ultimate"]
        queries = [
            [0, 4],  # All strings
            [1, 3],  # Middle subset
            [2, 2],  # Single string
        ]
        expected = [4, 2, 1]  # "apple", "ice", "orange", "ultimate" are valid
        self.assertEqual(
            self.solution.vowelStrings(words, queries),
            expected,
            "Failed mixed cases test",
        )

    def test_boundary_queries(self):
        """Test queries that cover boundary conditions."""
        words = ["abc", "aba", "ece", "aa", "e"]
        queries = [
            [0, 0],  # First element
            [4, 4],  # Last element
            [0, 4],  # Full range
            [2, 2],  # Single middle element
            [1, 3],  # Middle range
        ]
        expected = [0, 1, 4, 1, 3]
        self.assertEqual(
            self.solution.vowelStrings(words, queries),
            expected,
            "Failed boundary queries test",
        )

    def test_performance(self):
        """Test performance with larger inputs."""
        # Generate a large test case
        words = ["a" * i for i in range(1, 1001)]  # 1000 words
        queries = [[i, i + 10] for i in range(0, 990, 10)]  # 99 queries

        # Measure execution time
        import time

        start_time = time.time()
        result = self.solution.vowelStrings(words, queries)
        execution_time = time.time() - start_time

        # Assert execution time is reasonable (e.g., under 1 second)
        self.assertLess(
            execution_time,
            1.0,
            f"Performance test failed: took {execution_time:.2f} seconds",
        )

        # Assert result length matches query length
        self.assertEqual(
            len(result),
            len(queries),
            "Performance test failed: incorrect result length",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
