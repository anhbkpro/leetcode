from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        once = [num for num, count in counter.items() if count == 1]
        return max(once) if once else -1
