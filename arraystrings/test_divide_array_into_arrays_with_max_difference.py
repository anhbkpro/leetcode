import unittest
from .divide_array_into_arrays_with_max_difference import Solution


class TestDivideArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_division(self):
        # Test case 1: Valid array that can be divided
        nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
        k = 2
        expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
        self.assertEqual(self.solution.divideArray(nums, k), expected)

    def test_invalid_division(self):
        # Test case 2: Array that cannot be divided due to difference > k
        nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
        k = 1
        expected = []
        self.assertEqual(self.solution.divideArray(nums, k), expected)

    def test_empty_array(self):
        # Test case 3: Empty array
        nums = []
        k = 2
        expected = []
        self.assertEqual(self.solution.divideArray(nums, k), expected)

    def test_single_group(self):
        # Test case 4: Array with exactly 3 elements
        nums = [1, 2, 3]
        k = 2
        expected = [[1, 2, 3]]
        self.assertEqual(self.solution.divideArray(nums, k), expected)

    def test_all_same_numbers(self):
        # Test case 5: Array with all same numbers
        nums = [1, 1, 1, 1, 1, 1]
        k = 0
        expected = [[1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.solution.divideArray(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
