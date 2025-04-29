import unittest
from .count_subarrays_where_max_element_appears_at_least_k_times import Solution


class TestCountSubarraysWhereMaxElementAppearsAtLeastKTimes(unittest.TestCase):
    def test_example_1(self):
        # nums = [1,3,2,3,3], k = 2
        # max_element = 3
        # Valid subarrays: [3,2,3], [3,2,3,3], [2,3,3], [3,3]
        nums = [1, 3, 2, 3, 3]
        self.assertEqual(Solution.count_sub_arrays(nums, 2), 6)

    def test_all_elements_are_max(self):
        # nums = [5,5,5], k = 2
        # All subarrays of length >= 2 are valid
        nums = [5, 5, 5]
        self.assertEqual(Solution.count_sub_arrays(nums, 2), 3)

    def test_no_valid_subarrays(self):
        # nums = [1,2,3], k = 4
        # max_element = 3, but k > count of max_element in array
        nums = [1, 2, 3]
        self.assertEqual(Solution.count_sub_arrays(nums, 4), 0)

    def test_single_element(self):
        # nums = [7], k = 1
        nums = [7]
        self.assertEqual(Solution.count_sub_arrays(nums, 1), 1)
        # nums = [7], k = 2
        self.assertEqual(Solution.count_sub_arrays(nums, 2), 0)

    def test_k_is_one(self):
        # Every subarray containing the max at least once
        nums = [1, 2, 3]
        self.assertEqual(Solution.count_sub_arrays(nums, 1), 3)

    def test_k_greater_than_length(self):
        nums = [1, 2, 3]
        self.assertEqual(Solution.count_sub_arrays(nums, 5), 0)

    def test_multiple_max_elements(self):
        nums = [4, 1, 4, 4, 2]
        self.assertEqual(Solution.count_sub_arrays(nums, 2), 7)


if __name__ == "__main__":
    unittest.main()
