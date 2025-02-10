import unittest
from stacks_and_queues.clear_digits import SolutionStackLike, SolutionInPlace


class BaseTestClearDigits:
    def setUp(self):
        self.solution = None

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
        # After all chars are removed, result is empty
        s = "ab123456"
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_special_characters(self):
        # Test with special characters
        # Digits remove special characters just like normal characters
        s = "!@#1$%^2"
        self.assertEqual(self.solution.clearDigits(s), "!@$%")

    def test_spaces(self):
        # Test with spaces
        # Digits remove spaces just like other characters
        s = "hello 1world 2"
        self.assertEqual(self.solution.clearDigits(s), "helloworld")


class TestClearDigitsStackLike(BaseTestClearDigits, unittest.TestCase):
    def setUp(self):
        self.solution = SolutionStackLike()

    def test_only_digits(self):
        # Test string with only digits
        # First digit is appended (empty stack), rest are ignored (empty stack)
        s = "12345"
        self.assertEqual(self.solution.clearDigits(s), "5")

    def test_digits_at_start(self):
        # Test with digits at the start
        # First digit is appended (empty stack), rest are ignored (empty stack)
        s = "123abc"
        self.assertEqual(self.solution.clearDigits(s), "3abc")


class TestClearDigitsInPlace(BaseTestClearDigits, unittest.TestCase):
    def setUp(self):
        self.solution = SolutionInPlace()

    def test_only_digits(self):
        # Test string with only digits
        # All digits are ignored since there's nothing to remove
        s = "12345"
        self.assertEqual(self.solution.clearDigits(s), "")

    def test_digits_at_start(self):
        # Test with digits at the start
        # Digits at start are ignored since there's nothing to remove
        s = "123abc"
        self.assertEqual(self.solution.clearDigits(s), "abc")

    def test_large_string(self):
        # Test with a large string to verify in-place efficiency
        s = "a" * 1000 + "1" * 500
        expected = "a" * 500
        self.assertEqual(self.solution.clearDigits(s), expected)

    def test_no_modifications(self):
        # Test when no modifications are needed
        # This verifies the in-place algorithm correctly handles the case
        s = "abcdef"
        self.assertEqual(self.solution.clearDigits(s), s)

    def test_all_removed(self):
        # Test when all characters are removed
        # This verifies the in-place algorithm correctly handles empty result
        s = "a1b2c3"
        self.assertEqual(self.solution.clearDigits(s), "")


if __name__ == "__main__":
    unittest.main()
