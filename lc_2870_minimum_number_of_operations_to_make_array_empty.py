import collections
from math import ceil
from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
