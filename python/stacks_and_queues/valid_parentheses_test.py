import unittest
from .valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()"
        expected = True
        self.assertEqual(self.solution.isValid(s), expected)

    def test_example_2(self):
        s = "()[]{}"
        expected = True
        self.assertEqual(self.solution.isValid(s), expected)

    def test_example_3(self):
        s = "(]"
        expected = False
        self.assertEqual(self.solution.isValid(s), expected)

    def test_example_4(self):
        s = "([)]"
        expected = False
        self.assertEqual(self.solution.isValid(s), expected)

    def test_empty_path(self):
        s = ""
        expected = True
        self.assertEqual(self.solution.isValid(s), expected)


if __name__ == "__main__":
    unittest.main()
