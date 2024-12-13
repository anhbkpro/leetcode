from typing import List


class Solution:
    def is_possible(self, max_length: int, ribbons: List[int], k: int) -> bool:
        cut_ribbons = 0
        for ribbon in ribbons:
            cut_ribbons += ribbon // max_length

        return cut_ribbons >= k

    def maxLength(self, ribbons: List[int], k: int) -> int:
        ans = 0
        left, right = 1, max(ribbons)
        while left <= right:
            middle = (left + right) // 2
            if self.is_possible(middle, ribbons, k):
                ans = middle
                left = middle + 1
            else:
                right = middle - 1

        return ans
