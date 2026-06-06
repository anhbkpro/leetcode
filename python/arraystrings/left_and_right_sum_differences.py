from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        prefix_sum = 0
        ans = [0] * n
        for i in range(n):
            ans[i] = abs(total - nums[i] - 2 * prefix_sum)
            prefix_sum += nums[i]
        return ans

