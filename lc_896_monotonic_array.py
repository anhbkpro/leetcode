# My Solution
from typing import List


class Solution:
    @staticmethod
    def isMonotonic(nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        prev_diff = 0

        for i in range(len(nums) - 1):
            current_diff = nums[i + 1] - nums[i]
            if current_diff * prev_diff < 0:
                return False
            if current_diff == 0:
                continue
            prev_diff = current_diff

        return True