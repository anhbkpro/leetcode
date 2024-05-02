from collections import Counter
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = -1
        for k in counter:
            if -k in counter:
                ans = max(ans, k)

        return ans
