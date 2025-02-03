from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        local_decrease = 1
        local_increase = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                local_decrease += 1
                local_increase = 1
            elif nums[i] > nums[i - 1]:
                local_decrease = 1
                local_increase += 1
            else:
                local_increase = 1
                local_decrease = 1
            max_length = max(max_length, local_decrease, local_increase)

        return max_length
