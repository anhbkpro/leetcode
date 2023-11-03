from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i]] += 1

        for (k, v) in freq.items():
            if v > n / 2:
                return k

        return -1
