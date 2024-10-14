from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            new_stick = stick1 + stick2
            cost += new_stick
            heapq.heappush(sticks, new_stick)

        return cost
