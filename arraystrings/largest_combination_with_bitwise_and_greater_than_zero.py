from collections import defaultdict
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        can_bin = [bin(x)[2:] for x in candidates]
        m = defaultdict()
        for can in can_bin:
            n = len(can) - 1
            for i, c in enumerate(can):
                if c != "0":
                    m[n - i] = m.get(n - i, 0) + 1
        return max(m.values())
