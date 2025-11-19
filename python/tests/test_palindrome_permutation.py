import unittest
from hashing.palindrome_permutation import Solution


class TestPalindromePermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_functionality(self):
        # Test basic palindrome permutations
        self.assertTrue(self.solution.canPermutePalindrome("aab"))  # Can form "aba"
        self.assertFalse(
            self.solution.canPermutePalindrome("code")
        )  # Cannot form palindrome
        self.assertTrue(
            self.solution.canPermutePalindrome("carerac")
        )  # Can form "racecar"

    def test_edge_cases(self):
        # Test empty string and single character
        self.assertTrue(
            self.solution.canPermutePalindrome("")
        )  # Empty string is palindrome
        self.assertTrue(
            self.solution.canPermutePalindrome("a")
        )  # Single char is palindrome

        # Test two identical characters
        self.assertTrue(self.solution.canPermutePalindrome("aa"))  # Can form "aa"

    def test_special_cases(self):
        # Test all same characters
        self.assertTrue(self.solution.canPermutePalindrome("aaaa"))  # Can form "aaaa"

        # Test alternating characters
        self.assertTrue(self.solution.canPermutePalindrome("abab"))  # Can form "abba"

        # Test string with even occurrences of each character
        self.assertTrue(
            self.solution.canPermutePalindrome("abccba")
        )  # Can form "abccba"

    def test_case_sensitivity(self):
        # Test case sensitivity - 'A' and 'a' are different characters
        self.assertFalse(
            self.solution.canPermutePalindrome("AaBb")
        )  # Cannot form palindrome
        self.assertFalse(
            self.solution.canPermutePalindrome("Aa")
        )  # Different characters
        self.assertTrue(self.solution.canPermutePalindrome("aAaA"))  # Can form "aAAa"

    def test_special_characters(self):
        # Test with spaces and special characters as distinct characters
        self.assertTrue(self.solution.canPermutePalindrome("  "))  # Two spaces
        self.assertTrue(
            self.solution.canPermutePalindrome(" a ")
        )  # Two spaces, one letter - can form " a "
        self.assertTrue(self.solution.canPermutePalindrome("!@!"))  # Special characters
        self.assertFalse(
            self.solution.canPermutePalindrome("!@#")
        )  # Three different special chars


if __name__ == "__main__":
    unittest.main()
