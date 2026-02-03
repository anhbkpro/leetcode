from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # 1 = increasing, -1 = decreasing
        direction = 1
        turns = 1

        if nums[1] <= nums[0]:
            return False  # must start increasing

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff == 0:
                return False  # must be strictly monotonic

            if diff > 0 and direction == -1:
                direction = 1
                turns += 1
            elif diff < 0 and direction == 1:
                direction = -1
                turns += 1

        return turns == 3
