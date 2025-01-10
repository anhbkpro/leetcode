import unittest
from .word_subsets import Solution


class TestWordSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from the problem statement"""
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        expected = ["facebook", "google", "leetcode"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)  # Order doesn't matter

    def test_example_2(self):
        """Test the second example from the problem statement"""
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        expected = ["apple", "google", "leetcode"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_empty_words2(self):
        """Test when words2 is empty - all words1 should be universal"""
        words1 = ["test", "hello", "world"]
        words2 = []
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, words1)

    def test_no_universal_words(self):
        """Test when no words in words1 are universal"""
        words1 = ["cat", "dog", "bird"]
        words2 = ["xyz"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertEqual(result, [])

    def test_single_character_words(self):
        """Test with single character words"""
        words1 = ["a", "b", "ab", "bc"]
        words2 = ["a"]
        expected = ["a", "ab"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_repeated_characters(self):
        """Test with words containing repeated characters"""
        words1 = ["hello", "world", "leetcode"]
        words2 = ["ll"]
        expected = ["hello"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_multiple_conditions(self):
        """Test with multiple words in words2 with overlapping characters"""
        words1 = ["warrior", "world", "water", "well"]
        words2 = ["wr", "r"]
        expected = ["warrior", "world", "water"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_max_constraints(self):
        """Test with inputs near the maximum constraints"""
        # Create a word with 10 characters (max length)
        words1 = ["abcdefghij"] * 10  # 10 identical words
        words2 = ["abc", "def"]  # Multiple words with max length < 10
        result = self.solution.wordSubsets(words1, words2)
        self.assertTrue(all(len(word) <= 10 for word in result))

    def test_case_sensitivity(self):
        """Test that the solution handles only lowercase letters"""
        words1 = ["hello", "world"]
        words2 = ["h", "o"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertTrue(all(word.islower() for word in result))

    def test_subset_with_higher_frequency(self):
        """Test when words2 contains a character with higher frequency than words1"""
        words1 = ["hello", "world"]
        words2 = ["ll"]  # requires two 'l's
        expected = ["hello"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_overlapping_requirements(self):
        """Test with overlapping requirements in words2"""
        words1 = ["meeting", "motorcycle", "mountain"]
        words2 = ["mt", "t", "m"]
        expected = ["meeting", "motorcycle", "mountain"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)

    def test_all_unique_chars(self):
        """Test with words containing all unique characters"""
        words1 = ["abcde", "fghij", "klmno"]
        words2 = ["abc"]
        expected = ["abcde"]
        result = self.solution.wordSubsets(words1, words2)
        self.assertCountEqual(result, expected)


def run_tests():
    unittest.main()


if __name__ == "__main__":
    run_tests()
