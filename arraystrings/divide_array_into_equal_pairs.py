from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        return all(v % 2 == 0 for v in freq.values())
