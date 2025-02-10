import unittest
from stacks_and_queues.clear_digits import Solution


class TestClearDigits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        # Test basic case with mixed characters and digits
        # When digit is encountered and stack is not empty, it removes the previous character
        s = "ab1c2d"
        self.assertEqual(self.solution.clearDigits(s), "ad")

    def test_consecutive_digits(self):
        # Test with consecutive digits
        # Each digit removes one previous character until stack is empty
        s = "abc123"
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_no_digits(self):
        # Test string without any digits
        # No characters should be removed
        s = "abcdef"
        self.assertEqual(self.solution.clearDigits(s), "abcdef")

    def test_only_digits(self):
        # Test string with only digits
        # First digit is appended (empty stack), rest are ignored (empty stack)
        s = "12345"
        self.assertEqual(self.solution.clearDigits(s), "5")

    def test_empty_string(self):
        # Test empty string
        s = ""
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_alternating_chars_and_digits(self):
        # Test alternating characters and digits
        # Each digit removes the previous character
        s = "a1b2c3d4"
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_more_digits_than_chars(self):
        # Test case where there are more digits than characters
        # After all chars are removed, last digit is appended to empty stack
        s = "ab123456"
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_spaces(self):
        # Test with spaces
        # Digits remove spaces just like other characters
        s = "hello 1world 2"
        self.assertEqual(self.solution.clearDigits(s), "helloworld")

    def test_digits_at_start(self):
        # Test with digits at the start
        # First digit is appended (empty stack), rest are ignored (empty stack)
        s = "123abc"
        self.assertEqual(self.solution.clearDigits(s), "3abc")


if __name__ == "__main__":
    unittest.main()
