from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter(s2)
        if s1_counter != s2_counter:
            return False

        swaps = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                swaps += 1

        return swaps <= 2