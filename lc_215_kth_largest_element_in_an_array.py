import heapq
from typing import List


class Solution:
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)  # or return heap[0]
