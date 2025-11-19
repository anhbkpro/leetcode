import unittest
from delete_characters_to_make_fancy_string import Solution


class TestMakeFancyString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test with empty string"""
        self.assertEqual(self.solution.makeFancyString(""), "")

    def test_single_character(self):
        """Test with single character"""
        self.assertEqual(self.solution.makeFancyString("a"), "a")

    def test_two_characters(self):
        """Test with two characters"""
        self.assertEqual(self.solution.makeFancyString("aa"), "aa")
        self.assertEqual(self.solution.makeFancyString("ab"), "ab")

    def test_three_identical_characters(self):
        """Test with three identical characters"""
        self.assertEqual(self.solution.makeFancyString("aaa"), "aa")
        self.assertEqual(self.solution.makeFancyString("bbb"), "bb")

    def test_four_identical_characters(self):
        """Test with four identical characters"""
        self.assertEqual(self.solution.makeFancyString("aaaa"), "aa")
        self.assertEqual(self.solution.makeFancyString("bbbb"), "bb")

    def test_five_identical_characters(self):
        """Test with five identical characters"""
        self.assertEqual(self.solution.makeFancyString("aaaaa"), "aa")
        self.assertEqual(self.solution.makeFancyString("bbbbb"), "bb")

    def test_mixed_characters_with_consecutive(self):
        """Test with mixed characters and consecutive duplicates"""
        self.assertEqual(self.solution.makeFancyString("aaabbb"), "aabb")
        self.assertEqual(self.solution.makeFancyString("aaabbbccc"), "aabbcc")

    def test_consecutive_groups_separated(self):
        """Test with consecutive groups separated by other characters"""
        self.assertEqual(self.solution.makeFancyString("aaabaa"), "aabaa")
        self.assertEqual(self.solution.makeFancyString("aaabbbaa"), "aabbaa")

    def test_no_consecutive_duplicates(self):
        """Test with no consecutive duplicates"""
        self.assertEqual(self.solution.makeFancyString("abc"), "abc")
        self.assertEqual(self.solution.makeFancyString("abcdef"), "abcdef")

    def test_two_consecutive_duplicates(self):
        """Test with exactly two consecutive duplicates"""
        self.assertEqual(self.solution.makeFancyString("aab"), "aab")
        self.assertEqual(self.solution.makeFancyString("aabb"), "aabb")

    def test_complex_patterns(self):
        """Test with complex patterns"""
        self.assertEqual(self.solution.makeFancyString("aaabaaab"), "aabaab")
        self.assertEqual(self.solution.makeFancyString("aaabbbaaabbb"), "aabbaabb")
        self.assertEqual(self.solution.makeFancyString("aaabbbcccaaabbb"), "aabbccaabb")

    def test_numbers_and_special_characters(self):
        """Test with numbers and special characters"""
        self.assertEqual(self.solution.makeFancyString("111"), "11")
        self.assertEqual(self.solution.makeFancyString("!!!"), "!!")
        self.assertEqual(self.solution.makeFancyString("aa1aa"), "aa1aa")

    def test_long_strings(self):
        """Test with longer strings"""
        long_string = "a" * 100
        expected = "aa"
        self.assertEqual(self.solution.makeFancyString(long_string), expected)

    def test_leetcode_example(self):
        """Test with LeetCode example"""
        self.assertEqual(self.solution.makeFancyString("leeetcode"), "leetcode")
        self.assertEqual(self.solution.makeFancyString("aaabaaaa"), "aabaa")

    def test_edge_cases(self):
        """Test various edge cases"""
        # Single character repeated many times
        self.assertEqual(self.solution.makeFancyString("a" * 10), "aa")

        # Alternating characters
        self.assertEqual(self.solution.makeFancyString("ababab"), "ababab")

        # Two characters alternating with three consecutive
        self.assertEqual(self.solution.makeFancyString("abaaab"), "abaab")

    def test_unicode_characters(self):
        """Test with unicode characters"""
        self.assertEqual(self.solution.makeFancyString("😀😀😀"), "😀😀")
        self.assertEqual(self.solution.makeFancyString("🚀🚀🚀🚀"), "🚀🚀")

    def test_mixed_case(self):
        """Test with mixed case characters"""
        self.assertEqual(self.solution.makeFancyString("AAA"), "AA")
        self.assertEqual(self.solution.makeFancyString("AaA"), "AaA")
        self.assertEqual(self.solution.makeFancyString("aaA"), "aaA")

    def test_spaces_and_punctuation(self):
        """Test with spaces and punctuation"""
        self.assertEqual(self.solution.makeFancyString("   "), "  ")
        self.assertEqual(self.solution.makeFancyString("..."), "..")
        self.assertEqual(self.solution.makeFancyString("a a a"), "a a a")


if __name__ == "__main__":
    unittest.main()
