import unittest

from .lexicographically_minimum_string_after_removing_stars import Solution


class TestLexicographicallyMinimumStringAfterRemovingStars(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        s = "aaba*"
        expected = "aab"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_multiple_stars(self):
        s = "leet**cod*e"
        expected = "ltode"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_consecutive_stars(self):
        s = "erase*****"
        expected = ""
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_no_stars(self):
        s = "leetcode"
        expected = "leetcode"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_only_stars(self):
        s = "****"
        expected = ""
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_single_character(self):
        s = "a"
        expected = "a"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_single_star(self):
        s = "a*"
        expected = ""
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_lexicographical_order(self):
        s = "abc*"
        expected = "bc"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_multiple_same_characters(self):
        s = "aaa*"
        expected = "aa"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_complex_case(self):
        s = "a*b*c*d*"
        expected = ""
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_star_at_beginning(self):
        s = "*abc"
        expected = "abc"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_star_at_end(self):
        s = "abc*"
        expected = "bc"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_stars_in_middle(self):
        s = "ab*c*d"
        expected = "cd"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_leetcode_example(self):
        s = "leet**cod*e"
        expected = "ltode"
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(self.solution.clearStars(s), expected)

    def test_all_lowercase_letters(self):
        s = "abcdefghijklmnopqrstuvwxyz*"
        expected = "bcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.solution.clearStars(s), expected)


if __name__ == "__main__":
    unittest.main()
