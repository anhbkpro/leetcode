from typing import List
import heapq
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)

        heapq.heapify(heap)
        ans = 0
        for i in range(k):
            item = heapq.heappop(heap)
            ans += -item
            heapq.heappush(heap, ceil(item) // 3)

        return ans
