import heapq
from typing import List


class Solution:
    @staticmethod
    def kth_smallest(matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in range(len(matrix)):
            for num in matrix[row]:
                heapq.heappush(heap, -num)
                while len(heap) > k:
                    heapq.heappop(heap)

        return -heap[0]
