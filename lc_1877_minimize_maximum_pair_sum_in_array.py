from typing import List


class Solution:
    @staticmethod
    def minPairSum(nums: List[int]) -> int:
        nums.sort()

        max_sum = 0
        for i in range(len(nums)):
            max_sum = max(max_sum, nums[i] + nums[len(nums) - 1 - i])

        return max_sum
