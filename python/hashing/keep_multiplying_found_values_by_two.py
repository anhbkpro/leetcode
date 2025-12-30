from collections import Counter
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = Counter(nums)
        while original in s:
            original *= 2
        return original
