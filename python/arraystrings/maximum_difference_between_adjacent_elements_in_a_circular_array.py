from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        ans = float("-inf")
        for i in range(len(nums)):
            ans = max(ans, abs(nums[i] - nums[i - 1]))

        return ans
