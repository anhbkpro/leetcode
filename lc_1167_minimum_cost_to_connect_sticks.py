import heapq
from typing import List


class Solution:
    @staticmethod
    def connect_sticks(sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:
            joined_stick_cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            total_cost += joined_stick_cost
            heapq.heappush(sticks, joined_stick_cost)

        return total_cost
