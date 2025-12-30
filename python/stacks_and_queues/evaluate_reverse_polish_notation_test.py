import unittest

from .evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9  # ((2 + 1) * 3) = 9
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6  # (4 + (13 / 5)) = 6
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22  # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_single_number(self):
        tokens = ["42"]
        expected = 42
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_simple_addition(self):
        tokens = ["3", "4", "+"]
        expected = 7
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_simple_subtraction(self):
        tokens = ["3", "4", "-"]
        expected = -1
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_simple_multiplication(self):
        tokens = ["3", "4", "*"]
        expected = 12
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_simple_division(self):
        tokens = ["12", "3", "/"]
        expected = 4
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_division_truncate_toward_zero(self):
        tokens = ["7", "-3", "/"]
        expected = -2  # 7/(-3) = -2.333... should truncate toward zero
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_negative_numbers(self):
        tokens = ["-3", "-4", "+"]
        expected = -7
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_zero_division(self):
        tokens = ["0", "3", "/"]
        expected = 0
        self.assertEqual(self.solution.evalRPN(tokens), expected)

    def test_complex_expression(self):
        tokens = ["5", "2", "4", "*", "+", "7", "-"]
        expected = 6  # (5 + (2 * 4)) - 7 = 13 - 7 = 6
        self.assertEqual(self.solution.evalRPN(tokens), expected)


if __name__ == "__main__":
    unittest.main()
