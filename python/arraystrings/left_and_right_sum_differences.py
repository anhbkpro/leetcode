from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        prefix_sum = 0
        ans = []
        for i in range(len(nums)):
            ans.append(abs(total - nums[i] - 2 * prefix_sum))
            prefix_sum += nums[i]
        return ans
