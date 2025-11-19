import unittest
from .using_a_robot_to_print_the_lexicographically_smallest_string import Solution


class TestRobotWithString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        s = "zza"
        expected = "azz"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_sorted_string(self):
        s = "abc"
        expected = "abc"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_reverse_sorted_string(self):
        s = "cba"
        expected = "abc"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_single_character(self):
        s = "a"
        expected = "a"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_repeated_characters(self):
        s = "aaa"
        expected = "aaa"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_complex_case(self):
        s = "bac"
        expected = "abc"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_leetcode_example(self):
        s = "bdda"
        expected = "addb"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_all_same_characters_different_case(self):
        s = "zzzzz"
        expected = "zzzzz"
        self.assertEqual(self.solution.robotWithString(s), expected)

    def test_mixed_case(self):
        s = "bdaac"
        expected = "aacdb"
        self.assertEqual(self.solution.robotWithString(s), expected)


if __name__ == "__main__":
    unittest.main()
