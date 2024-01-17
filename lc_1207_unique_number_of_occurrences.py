from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq.keys()) == len(set(freq.values()))
