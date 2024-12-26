from .target_sum import Solution


import unittest


class TestTargetSumWays(unittest.TestCase):
    def setUp(self):
        """Initialize a new Solution instance before each test"""
        self.solution = Solution()

    def test_basic_example(self):
        """Test with a basic example where there are multiple ways to reach target"""
        nums = [1, 1, 1, 1, 1]
        target = 3
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 5)

    def test_single_number(self):
        """Test with a single number where target can be reached in exactly one way"""
        nums = [5]
        target = 5
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)

    def test_no_solution(self):
        """Test when target cannot be reached"""
        nums = [1, 2, 3]
        target = 10
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 0)

    def test_zero_target(self):
        """Test with target of zero"""
        nums = [1, 0]
        target = 0
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 0)

    def test_negative_target(self):
        """Test with negative target value"""
        nums = [1, 2, 1]
        target = -2
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 2)

    def test_large_numbers(self):
        """Test with larger numbers"""
        nums = [10, 20, 30]
        target = 60
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)

    def test_multiple_calls(self):
        """Test that multiple calls to findTargetSumWays work correctly"""
        nums1 = [1, 1]
        target1 = 0
        nums2 = [1, 2]
        target2 = 3

        result1 = self.solution.findTargetSumWays(nums1, target1)
        result2 = self.solution.findTargetSumWays(nums2, target2)

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    def test_all_zeros(self):
        """Test with array containing all zeros"""
        nums = [0, 0, 0]
        target = 0
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 8)

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        target = 0
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)

    def test_large_array(self):
        """Test with a larger array"""
        nums = [1] * 10  # Array of 10 ones
        target = 0
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 252)

    def test_max_sum_target(self):
        """Test with target equal to maximum possible sum"""
        nums = [1, 2, 3]
        target = 6  # 1 + 2 + 3
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)

    def test_min_sum_target(self):
        """Test with target equal to minimum possible sum"""
        nums = [1, 2, 3]
        target = -6  # -1 - 2 - 3
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
