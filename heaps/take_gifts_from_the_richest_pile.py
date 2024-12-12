import heapq
from math import floor, sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_heap = []
        for gift in gifts:
            heapq.heappush(gifts_heap, -gift)

        for i in range(k):
            item = heapq.heappop(gifts_heap)
            left_gift = floor(sqrt(-item))
            heapq.heappush(gifts_heap, -left_gift)

        return -sum(gifts_heap)
