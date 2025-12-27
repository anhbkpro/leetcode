import heapq
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-h for h in happiness]
        heapq.heapify(max_heap)

        total_happiness_sum = 0
        turn = 0

        # Can only select up to min(k, len(happiness)) children
        for i in range(min(k, len(happiness))):
            total_happiness_sum += max(-(heapq.heappop(max_heap)) - turn, 0)
            turn += 1

        return total_happiness_sum

