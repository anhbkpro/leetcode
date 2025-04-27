import unittest
from .count_subarrays_of_length_three_with_a_condition import Solution


class TestCountSubarraysOfLengthThreeWithACondition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_less_than_three_elements(self):
        self.assertEqual(self.solution.countSubarrays([]), 0)
        self.assertEqual(self.solution.countSubarrays([1]), 0)
        self.assertEqual(self.solution.countSubarrays([1, 2]), 0)

    def test_no_valid_subarrays(self):
        self.assertEqual(self.solution.countSubarrays([1, 2, 3]), 0)
        self.assertEqual(self.solution.countSubarrays([10, 20, 30, 40]), 0)

    def test_one_valid_subarray(self):
        # nums[0] + nums[2] == nums[1] / 2 for [2, 8, 2]: 2+2 == 8/2 -> 4 == 4
        self.assertEqual(self.solution.countSubarrays([2, 8, 2]), 1)

    def test_all_elements_same(self):
        # [4, 4, 4]: 4+4 == 4/2 -> 8 == 2 (not valid)
        self.assertEqual(self.solution.countSubarrays([4, 4, 4]), 0)

    def test_negative_numbers(self):
        # [-2, -8, -2]: -2 + -2 == -8/2 -> -4 == -4
        self.assertEqual(self.solution.countSubarrays([-2, -8, -2]), 1)

    def test_longer_array(self):
        # [2, 8, 2, 8, 2]: [2,8,2] and [8,2,8] and [2,8,2] are valid
        self.assertEqual(self.solution.countSubarrays([2, 8, 2, 8, 2]), 2)


if __name__ == "__main__":
    unittest.main()
