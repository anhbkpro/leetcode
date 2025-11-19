from typing import List


class Solution:
    def _can_allocate_candies(
        self, candies: List[int], k: int, num_of_candies: int
    ) -> bool:
        max_num_of_children = 0
        for pile in candies:
            max_num_of_children += pile // num_of_candies
        return max_num_of_children >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        left, right = 1, max(candies)
        while left < right:
            middle = (left + right + 1) // 2
            if self._can_allocate_candies(candies, k, middle):
                left = middle
            else:
                right = middle - 1
        return left
