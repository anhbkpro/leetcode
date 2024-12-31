from typing import List


class Solution:
    def is_possible(self, max_length: int, ribbons: List[int], k: int) -> bool:
        cut_ribbons = sum(ribbon // max_length for ribbon in ribbons)
        return cut_ribbons >= k

    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 0, max(ribbons)
        while left < right:
            middle = (left + right) // 2
            if self.is_possible(middle, ribbons, k):
                left = middle
            else:
                right = middle - 1

        return left
