import unittest

from .valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))
        self.assertTrue(self.solution.isPalindrome("   "))

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome("A"))
        self.assertTrue(self.solution.isPalindrome("1"))

    def test_valid_palindromes(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solution.isPalindrome("race a car"))
        self.assertTrue(self.solution.isPalindrome("Was it a car or a cat I saw?"))
        self.assertTrue(self.solution.isPalindrome("12321"))
        self.assertTrue(self.solution.isPalindrome("Madam, I'm Adam"))

    def test_invalid_palindromes(self):
        self.assertFalse(self.solution.isPalindrome("hello"))
        self.assertFalse(self.solution.isPalindrome("not a palindrome"))
        self.assertFalse(self.solution.isPalindrome("12345"))

    def test_special_characters(self):
        self.assertTrue(self.solution.isPalindrome(".,"))
        self.assertTrue(self.solution.isPalindrome("!@#$%^&*()"))
        self.assertTrue(self.solution.isPalindrome("a."))
        self.assertTrue(self.solution.isPalindrome(".a"))

    def test_mixed_case(self):
        self.assertTrue(self.solution.isPalindrome("Aba"))
        self.assertTrue(self.solution.isPalindrome("aBa"))
        self.assertFalse(self.solution.isPalindrome("aBc"))


if __name__ == "__main__":
    unittest.main()
