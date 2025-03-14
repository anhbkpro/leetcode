from typing import List


class Solution:
    def _can_allocate(self, candies: List[int], k: int, pivot: int) -> bool:
        number_of_sub_piles = 0
        for candie in candies:
            number_of_sub_piles += candie // pivot
        return number_of_sub_piles >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        left, right = 1, max(candies)
        while left <= right:
            mid = (left + right) // 2
            if self._can_allocate(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
