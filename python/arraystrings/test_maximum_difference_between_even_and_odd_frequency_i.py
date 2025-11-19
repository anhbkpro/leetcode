import unittest
from .maximum_difference_between_even_and_odd_frequency_i import Solution


class TestMaximumDifferenceBetweenEvenAndOddFrequency(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        s = "aab"
        expected = -1
        self.assertEqual(self.solution.maxDifference(s), expected)

    def test_mixed_frequencies(self):
        s = "aabbc"
        expected = -1
        self.assertEqual(self.solution.maxDifference(s), expected)

    def test_leetcode_example(self):
        s = "aab"
        expected = -1
        self.assertEqual(self.solution.maxDifference(s), expected)

    def test_multiple_even_odd_pairs(self):
        s = "aabbccd"
        expected = -1
        self.assertEqual(self.solution.maxDifference(s), expected)

    def test_string_length_less_than_three(self):
        s = "ab"
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)

    def test_string_length_greater_than_hundred(self):
        s = "a" * 101
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)

    def test_uppercase_letters(self):
        s = "Aab"
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)

    def test_non_letter_characters(self):
        s = "a1b"
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)

    def test_all_even_frequencies(self):
        s = "aabbcc"
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)

    def test_all_odd_frequencies(self):
        s = "abc"
        with self.assertRaises(ValueError):
            self.solution.maxDifference(s)


if __name__ == "__main__":
    unittest.main()
