from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        max_odd = max([x for x in cnt.values() if x % 2 == 1])
        min_even = min([x for x in cnt.values() if x % 2 == 0])
        return max_odd - min_even
