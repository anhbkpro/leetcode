from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < 2:
            return 0

        # Create a min heap
        heapify(nums)
        num_operations = 0

        # Continue while we have at least 2 elements and smallest element < k
        while len(nums) >= 2 and nums[0] < k:
            # Get two smallest elements
            x = heappop(nums)
            y = heappop(nums)

            # Create new value: min(x,y) * 2 + max(x,y)
            new_val = min(x, y) * 2 + max(x, y)
            heappush(nums, new_val)
            num_operations += 1

        # Check if we succeeded in making all elements >= k
        return num_operations if nums and nums[0] >= k else -1
