import unittest
from .make_the_prefix_sum_non_negative import Solution


class TestMakePrefixSumNonNegative(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, -5, 1, -4, 3, -2]
        expected = 2
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_example_2(self):
        nums = [-2, 2, -3, 1]
        expected = 2
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_empty_array(self):
        nums = []
        expected = 0
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_all_negative(self):
        nums = [-1, -2, -3, -4, -5]
        expected = 5
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_alternating_numbers(self):
        nums = [1, -1, 1, -1, 1, -1]
        expected = 0
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_large_negative_first(self):
        nums = [-10, 1, 1, 1]
        expected = 1
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_multiple_negatives_in_sequence(self):
        nums = [1, -2, -3, -4, 5]
        expected = 3
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_zero_elements(self):
        nums = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_single_element_negative(self):
        nums = [-5]
        expected = 1
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_single_element_positive(self):
        nums = [5]
        expected = 0
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)

    def test_complex_sequence(self):
        nums = [3, -4, 2, -5, -2, 6, -3]
        expected = 2
        self.assertEqual(self.solution.makePrefSumNonNegative(nums), expected)


if __name__ == "__main__":
    unittest.main()
