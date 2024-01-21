from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.rob_from(0, nums)

    def rob_from(self, index, nums):
        # No more houses left to rob
        if index >= len(nums):
            return 0

        if index in self.memo:
            return self.memo[index]

        ans = max(self.rob_from(index + 1, nums), self.rob_from(index + 2, nums) + nums[index])

        self.memo[index] = ans
        return ans
