import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num for num in nums]
        heapq.heapify(heap)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heap[0]
