from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def max_frequency_elements(nums: List[int]) -> int:
        max_freq = 0
        freq = Counter(nums)
        for k in freq:
            max_freq = max(max_freq, freq[k])
        return sum([freq[k] for k in freq if freq[k] == max_freq])