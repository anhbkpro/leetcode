from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        avg = total / k
        for r in range(k, len(nums)):
            total += (nums[r] - nums[r - k])
            avg = max(avg, total/k)

        return avg
