import unittest

from .counting_words_with_a_given_prefix import SolutionBuiltIn, SolutionTrie


class TestPrefixCount(unittest.TestCase):
    def setUp(self):
        # Initialize both solution instances
        self.solutions = [SolutionBuiltIn(), SolutionTrie()]

    def _test_all_solutions(self, words, pref, expected):
        """Helper method to test all solution implementations with the same input"""
        for solution in self.solutions:
            with self.subTest(solution_type=type(solution).__name__):
                result = solution.prefixCount(words, pref)
                self.assertEqual(
                    result,
                    expected,
                    f"Failed for {type(solution).__name__}: expected {expected}, got {result}",
                )

    def test_basic_prefix_matching(self):
        """Test basic prefix matching functionality"""
        words = ["apple", "app", "apricot", "banana"]
        self._test_all_solutions(words, "ap", 3)

    def test_empty_words_list(self):
        """Test behavior with empty words list"""
        self._test_all_solutions([], "test", 0)

    def test_no_matches(self):
        """Test when no words match the prefix"""
        words = ["apple", "banana", "cherry"]
        self._test_all_solutions(words, "z", 0)

    def test_single_character_words(self):
        """Test with single character words and prefixes"""
        words = ["a", "b", "a", "c"]
        self._test_all_solutions(words, "a", 2)

    def test_all_same_words(self):
        """Test with list containing identical words"""
        words = ["test", "test", "test"]
        self._test_all_solutions(words, "test", 3)

    def test_trie_specific_large_alphabet(self):
        """Test Trie solution with words using full lowercase alphabet"""
        words = ["abcdefghijklmnopqrstuvwxyz", "abcdef", "abc"]
        self._test_all_solutions(words, "abc", 3)

    def test_stress_test(self):
        """Test with larger input to check performance"""
        words = ["test"] * 1000 + ["other"] * 1000
        self._test_all_solutions(words, "test", 1000)


if __name__ == "__main__":
    unittest.main()
