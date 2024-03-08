from typing import List


class Solution:
    @staticmethod
    def max_frequency_elements(nums: List[int]) -> int:
        from collections import Counter

        c = Counter(nums)
        max_freq = max(c.values())
        return len([k for k, v in c.items() if v == max_freq])
