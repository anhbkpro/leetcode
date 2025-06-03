import unittest
from .LC75__determine_if_two_strings_are_close import Solution


class TestCloseStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_strings(self):
        self.assertTrue(self.solution.closeStrings("", ""))
        self.assertFalse(self.solution.closeStrings("", "a"))
        self.assertFalse(self.solution.closeStrings("a", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.closeStrings("a", "a"))
        self.assertFalse(self.solution.closeStrings("a", "b"))

    def test_same_characters_different_frequencies(self):
        # Test cases where strings have same characters but different frequencies
        self.assertTrue(self.solution.closeStrings("abc", "cba"))
        self.assertTrue(self.solution.closeStrings("aab", "bba"))
        self.assertTrue(self.solution.closeStrings("cabbba", "abbccc"))

    def test_different_characters(self):
        # Test cases where strings have different characters
        self.assertFalse(self.solution.closeStrings("abc", "def"))
        self.assertFalse(self.solution.closeStrings("a", "aa"))
        self.assertFalse(self.solution.closeStrings("aa", "ab"))

    def test_same_frequencies_different_characters(self):
        # Test cases where strings have same frequencies but different characters
        self.assertFalse(self.solution.closeStrings("abc", "def"))
        self.assertFalse(self.solution.closeStrings("aabb", "ccdd"))

    def test_complex_cases(self):
        # Test cases with longer strings and more complex patterns
        self.assertTrue(self.solution.closeStrings("cabbba", "abbccc"))
        self.assertFalse(self.solution.closeStrings("uau", "ssx"))
        self.assertFalse(self.solution.closeStrings("cabbba", "aabbss"))
        self.assertFalse(self.solution.closeStrings("uau", "ssy"))

    def test_edge_cases(self):
        # Test cases with special characters and numbers
        self.assertTrue(self.solution.closeStrings("123", "321"))
        self.assertTrue(self.solution.closeStrings("!@#", "#@!"))
        self.assertFalse(self.solution.closeStrings("123", "456"))
        self.assertFalse(self.solution.closeStrings("!@#", "!@$"))

    def test_case_sensitivity(self):
        # Test cases with different cases
        self.assertFalse(self.solution.closeStrings("abc", "ABC"))
        self.assertTrue(self.solution.closeStrings("aA", "Aa"))
        self.assertFalse(self.solution.closeStrings("Hello", "hello"))

    def test_repeated_characters(self):
        # Test cases with repeated characters
        self.assertTrue(self.solution.closeStrings("aaabbb", "bbbaaa"))
        self.assertTrue(self.solution.closeStrings("aaaaa", "aaaaa"))
        self.assertFalse(self.solution.closeStrings("aaaaa", "aaaab"))
        self.assertFalse(self.solution.closeStrings("aaabbb", "aaaccc"))


if __name__ == "__main__":
    unittest.main()
