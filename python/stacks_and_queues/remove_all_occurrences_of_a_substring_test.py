import unittest
from stacks_and_queues.remove_all_occurrences_of_a_substring import Solution


class TestRemoveOccurrences(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Test case from LeetCode example 1
        # Input: s = "daabcbaabcbc", part = "abc"
        # Output: "dab"
        s = "daabcbaabcbc"
        part = "abc"
        self.assertEqual(self.solution.removeOccurrences(s, part), "dab")

    def test_example_2(self):
        # Test case from LeetCode example 2
        # Input: s = "axxxxyyyyb", part = "xy"
        # Output: "ab"
        s = "axxxxyyyyb"
        part = "xy"
        self.assertEqual(self.solution.removeOccurrences(s, part), "ab")

    def test_no_occurrence(self):
        # Test when part doesn't exist in string
        s = "abcdef"
        part = "xyz"
        self.assertEqual(self.solution.removeOccurrences(s, part), "abcdef")

    def test_empty_string(self):
        # Test with empty string
        s = ""
        part = "abc"
        self.assertEqual(self.solution.removeOccurrences(s, part), "")

    def test_empty_part(self):
        # Test with empty part
        s = "abcdef"
        part = ""
        self.assertEqual(self.solution.removeOccurrences(s, part), "abcdef")

    def test_single_char_part(self):
        # Test with single character part
        s = "aaaa"
        part = "a"
        self.assertEqual(self.solution.removeOccurrences(s, part), "")

    def test_overlapping_occurrences(self):
        # Test with overlapping potential matches
        s = "aaaaa"
        part = "aa"
        self.assertEqual(self.solution.removeOccurrences(s, part), "a")

    def test_multiple_removals(self):
        # Test when multiple removals are needed
        s = "abcabcabc"
        part = "abc"
        self.assertEqual(self.solution.removeOccurrences(s, part), "")

    def test_part_longer_than_string(self):
        # Test when part is longer than string
        s = "abc"
        part = "abcd"
        self.assertEqual(self.solution.removeOccurrences(s, part), "abc")

    def test_repeated_chars(self):
        # Test with repeated characters in part
        s = "aababaab"
        part = "aab"
        self.assertEqual(self.solution.removeOccurrences(s, part), "ab")


if __name__ == "__main__":
    unittest.main()
