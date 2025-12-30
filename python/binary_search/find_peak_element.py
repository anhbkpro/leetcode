from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        r = len(nums) - 1
        while left < r:
            mid = (left + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                left = mid + 1
        return left
