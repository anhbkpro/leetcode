from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def distributeCandies(candyType: List[int]) -> int:
        candy_type = Counter(candyType)
        return min(len(candy_type), len(candyType) // 2)
