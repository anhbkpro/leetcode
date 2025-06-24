import unittest
from .find_all_k_distant_indices_in_an_array import Solution


class TestFindKDistantIndices(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: nums = [3,4,9,1,3,9,5], key = 9, k = 1"""
        # Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
        # Output: [1,2,3,4,5,6]
        # Explanation: Here, nums[2] == key and nums[5] == key.
        # - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
        # - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
        # - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
        # - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
        # - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
        # - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
        # - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
        # Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.
        nums = [3, 4, 9, 1, 3, 9, 5]
        key = 9
        k = 1
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.findKDistantIndices(nums, key, k), expected)

    def test_example_2(self):
        """Test Example 2: nums = [2,2,2,2,2], key = 2, k = 2"""
        # Input: nums = [2,2,2,2,2], key = 2, k = 2
        # Output: [0,1,2,3,4]
        # Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.
        # Hence, we return [0,1,2,3,4].
        nums = [2, 2, 2, 2, 2]
        key = 2
        k = 2
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(self.solution.findKDistantIndices(nums, key, k), expected)


if __name__ == "__main__":
    unittest.main()
