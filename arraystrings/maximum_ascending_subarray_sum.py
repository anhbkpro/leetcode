from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret_val = nums[0]
        window_sum = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            ret_val = max(ret_val, window_sum)
            if i < len(nums) - 1 and nums[i] >= nums[i + 1]:
                window_sum = 0

        return ret_val