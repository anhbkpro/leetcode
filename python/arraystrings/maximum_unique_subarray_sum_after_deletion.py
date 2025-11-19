from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive_keys = set([num for num in nums if num > 0])
        if positive_keys:
            return sum(positive_keys)

        return max(nums)
