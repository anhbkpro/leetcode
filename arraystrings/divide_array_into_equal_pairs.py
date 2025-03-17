from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for _, v in freq.items():
            if v % 2:
                return False
        return True
