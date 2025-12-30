import unittest
from typing import List, Type

from .count_prefix_and_suffix_pairs_i import SolutionBase, SolutionBF, SolutionTrie


class TestPrefixSuffixSolution(unittest.TestCase):
    def run_test_case(
        self, solution_class: Type[SolutionBase], words: List[str], expected: int
    ):
        """Helper method to run a test case for a specific solution class"""
        solution = solution_class()
        result = solution.countPrefixSuffixPairs(words)
        self.assertEqual(
            result,
            expected,
            f"{solution_class.__name__} failed: Expected {expected}, got {result}",
        )

    def run_all_solutions(self, words, expected):
        """Run the same test case for all solution classes"""
        solutions = [SolutionBF, SolutionTrie]
        for solution_class in solutions:
            self.run_test_case(solution_class, words, expected)

    def test_example_1(self):
        """Test case from Example 1"""
        words = ["a", "aba", "ababa", "aa"]
        self.run_all_solutions(words, 4)

    def test_example_2(self):
        """Test case from Example 2"""
        words = ["pa", "papa", "ma", "mama"]
        self.run_all_solutions(words, 2)

    def test_example_3(self):
        """Test case from Example 3"""
        words = ["abab", "ab"]
        self.run_all_solutions(words, 0)

    def test_single_word(self):
        """Test array with single word"""
        words = ["hello"]
        self.run_all_solutions(words, 0)

    def test_identical_words(self):
        """Test array with identical words"""
        words = ["abc", "abc", "abc"]
        self.run_all_solutions(words, 3)

    def test_no_matches(self):
        """Test array with no valid prefix-suffix pairs"""
        words = ["cat", "dog", "bird", "fish"]
        self.run_all_solutions(words, 0)

    def test_max_length_strings(self):
        """Test with maximum length strings (10 characters)"""
        words = ["abcdefghij", "abcdefghij", "abcdefghi"]
        self.run_all_solutions(words, 1)

    def test_nested_patterns(self):
        """Test with nested pattern strings"""
        words = ["a", "aa", "aaa", "aaaa"]
        # Count pairs: (a,aa), (a,aaa), (a,aaaa), (aa,aaa), (aa,aaaa), (aaa,aaaa)
        self.run_all_solutions(words, 6)

    def test_palindrome_patterns(self):
        """Test with palindrome strings"""
        words = ["aba", "ababa", "aabbaa"]
        self.run_all_solutions(words, 1)

    def test_different_lengths(self):
        """Test strings of different lengths"""
        words = ["a", "ab", "abc", "abcd"]
        self.run_all_solutions(words, 0)

    def test_constraints(self):
        """Test edge cases within constraints"""
        # Test maximum length array (50 elements)
        long_words = ["a"] * 50
        expected = (49 * 50) // 2  # Number of pairs when all words are identical
        self.run_all_solutions(long_words, expected)

        # Test maximum word length (10 characters)
        words = ["a" * 10, "a" * 10]
        self.run_all_solutions(words, 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
