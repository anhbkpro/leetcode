from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = len([num for num in nums if num < 0])
        positive_count = len([num for num in nums if num > 0])
        return max(negative_count, positive_count)
