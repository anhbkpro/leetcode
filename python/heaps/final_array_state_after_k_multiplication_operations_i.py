import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))

        for _ in range(k):
            _, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))

        return nums
