import unittest
from .count_subarrays_with_fixed_bounds import Solution


class TestCountSubarraysWithFixedBounds(unittest.TestCase):
    def test_example_1(self):
        # nums = [1,3,5,2,7,5], minK = 1, maxK = 5
        # Valid subarrays: [1,3,5], [1,3,5,2], [3,5], [5]
        nums = [1, 3, 5, 2, 7, 5]
        self.assertEqual(Solution.count_sub_arrays(nums, 1, 5), 2)

    def test_all_elements_in_range(self):
        # nums = [2,2,2], minK = 2, maxK = 2
        # Every subarray is valid
        nums = [2, 2, 2]
        self.assertEqual(Solution.count_sub_arrays(nums, 2, 2), 6)

    def test_no_valid_subarrays(self):
        # nums = [1,2,3], minK = 4, maxK = 5
        # No subarray contains both minK and maxK
        nums = [1, 2, 3]
        self.assertEqual(Solution.count_sub_arrays(nums, 4, 5), 0)

    def test_single_element(self):
        # nums = [5], minK = 5, maxK = 5
        nums = [5]
        self.assertEqual(Solution.count_sub_arrays(nums, 5, 5), 1)

    def test_multiple_valid_subarrays(self):
        # nums = [1,1,5,5,1,5], minK = 1, maxK = 5
        nums = [1, 1, 5, 5, 1, 5]
        self.assertEqual(Solution.count_sub_arrays(nums, 1, 5), 13)

    def test_minK_greater_than_maxK(self):
        # nums = [1,2,3,4], minK = 4, maxK = 1
        # No valid subarrays
        nums = [1, 2, 3, 4]
        self.assertEqual(Solution.count_sub_arrays(nums, 4, 1), 0)

    def test_negative_numbers(self):
        # nums = [-2,-1,0,1,2], minK = -2, maxK = 2
        nums = [-2, -1, 0, 1, 2]
        self.assertEqual(Solution.count_sub_arrays(nums, -2, 2), 1)


if __name__ == "__main__":
    unittest.main()
