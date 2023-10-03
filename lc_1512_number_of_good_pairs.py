from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def numIdenticalPairs(nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0

        for num in nums:
            ans += counts[num]
            counts[num] += 1

        return ans
