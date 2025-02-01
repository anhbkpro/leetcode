import unittest
from abc import ABC, abstractmethod
from special_array_i import Solution, SolutionModuloComparisons, SolutionBitwiseOperations


class BaseSpecialArrayTests:
    """Base test class containing test methods for special array implementations"""
    def test_empty_array(self):
        nums = []
        self.assertTrue(self.solution.isArraySpecial(nums))

    def test_single_element(self):
        nums = [1]
        self.assertTrue(self.solution.isArraySpecial(nums))

    def test_two_elements_valid(self):
        nums = [2, 3]  # even, odd
        self.assertTrue(self.solution.isArraySpecial(nums))

    def test_two_elements_invalid(self):
        nums = [2, 4]  # both even
        self.assertFalse(self.solution.isArraySpecial(nums))

    def test_multiple_elements_valid(self):
        nums = [2, 3, 4, 5]  # alternating even-odd
        self.assertTrue(self.solution.isArraySpecial(nums))

    def test_multiple_elements_invalid(self):
        nums = [2, 3, 5, 7]  # starts even-odd but then has two odds
        self.assertFalse(self.solution.isArraySpecial(nums))

    def test_negative_numbers(self):
        nums = [-2, -3, -4, -5]  # alternating even-odd with negatives
        self.assertTrue(self.solution.isArraySpecial(nums))

    def test_mixed_signs(self):
        nums = [-2, 3, -4, 5]  # alternating even-odd with mixed signs
        self.assertTrue(self.solution.isArraySpecial(nums))


class TestSpecialArray(unittest.TestCase, BaseSpecialArrayTests):
    def setUp(self):
        self.solution = Solution()


class TestSpecialArrayModulo(unittest.TestCase, BaseSpecialArrayTests):
    def setUp(self):
        self.solution = SolutionModuloComparisons()


class TestSpecialArrayBitwise(unittest.TestCase, BaseSpecialArrayTests):
    def setUp(self):
        self.solution = SolutionBitwiseOperations()


if __name__ == "__main__":
    unittest.main()
