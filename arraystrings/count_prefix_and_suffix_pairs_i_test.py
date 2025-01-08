import unittest
from .count_prefix_and_suffix_pairs_i import Solution


class TestPrefixSuffixSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_prefix_and_suffix_basic(self):
        """Test basic cases for isPrefixAndSuffix method"""
        test_cases = [
            ("aba", "ababa", True),
            ("abc", "abcd", False),
            ("a", "a", True),
            ("hello", "hello", True),
            ("ab", "abc", False),
            ("bc", "abc", False),
        ]

        for str1, str2, expected in test_cases:
            with self.subTest(str1=str1, str2=str2):
                result = self.solution.isPrefixAndSuffix(str1, str2)
                self.assertEqual(result, expected)

    def test_example_1(self):
        """Test case from Example 1"""
        words = ["a", "aba", "ababa", "aa"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 4)

    def test_example_2(self):
        """Test case from Example 2"""
        words = ["pa", "papa", "ma", "mama"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 2)

    def test_example_3(self):
        """Test case from Example 3"""
        words = ["abab", "ab"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 0)

    def test_single_word(self):
        """Test array with single word"""
        words = ["hello"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 0)

    def test_identical_words(self):
        """Test array with identical words"""
        words = ["abc", "abc", "abc"]
        self.assertEqual(
            self.solution.countPrefixSuffixPairs(words), 3
        )  # All pairs are valid

    def test_no_matches(self):
        """Test array with no valid prefix-suffix pairs"""
        words = ["cat", "dog", "bird", "fish"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 0)

    def test_max_length_strings(self):
        """Test with maximum length strings (10 characters)"""
        words = ["abcdefghij", "abcdefghij", "abcdefghi"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 1)

    def test_nested_patterns(self):
        """Test with nested pattern strings"""
        words = ["a", "aa", "aaa", "aaaa"]
        # Count pairs: (a,aa), (a,aaa), (a,aaaa), (aa,aaa), (aa,aaaa), (aaa,aaaa)
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 6)

    def test_palindrome_patterns(self):
        """Test with palindrome strings"""
        words = ["aba", "ababa", "aabbaa"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 1)

    def test_different_lengths(self):
        """Test strings of different lengths"""
        words = ["a", "ab", "abc", "abcd"]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 0)

    def test_constraints(self):
        """Test edge cases within constraints"""
        # Test maximum length array (50 elements)
        long_words = ["a"] * 50
        result = self.solution.countPrefixSuffixPairs(long_words)
        expected = (49 * 50) // 2  # Number of pairs when all words are identical
        self.assertEqual(result, expected)

        # Test maximum word length (10 characters)
        words = ["a" * 10, "a" * 10]
        self.assertEqual(self.solution.countPrefixSuffixPairs(words), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
