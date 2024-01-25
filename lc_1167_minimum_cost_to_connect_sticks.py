import heapq
from typing import List


class Solution:
    @staticmethod
    def connectSticks(sticks: List[int]) -> int:
        h = []
        for s in sticks:
            heapq.heappush(h, s)
        sum = 0
        while len(h) > 1:
            top_two_sum = heapq.heappop(h) + heapq.heappop(h)
            sum += top_two_sum
            heapq.heappush(h, top_two_sum)

        return sum
