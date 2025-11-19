from typing import List
from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        once = [num for num, count in counter.items() if count == 1]
        return max(once) if once else -1
