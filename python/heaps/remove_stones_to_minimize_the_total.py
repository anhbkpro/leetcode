from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]  # max heap
        heapify(heap)
        for _ in range(k):
            max_pile = -heappop(heap)
            new_pile = (max_pile + 1) // 2
            heappush(heap, -new_pile)

        return -sum(heap)
