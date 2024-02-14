import heapq
from typing import List


class Solution:
    @staticmethod
    def last_stone_weight(stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue

            heapq.heappush(stones, x - y)

        return -heapq.heappop(stones) if stones else 0

