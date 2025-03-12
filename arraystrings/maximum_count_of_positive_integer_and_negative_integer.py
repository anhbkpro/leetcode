from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = len([num for num in nums if num < 0])
        positive_count = len([num for num in nums if num > 0])
        return max(negative_count, positive_count)


class BinarySearchSolution:
    def _find_right_bound(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def _find_left_bound(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def maximumCount(self, nums: List[int]) -> int:
        last_negative_idx = self._find_left_bound(nums)
        first_positive_idx = self._find_right_bound(nums)
        return max(len(nums) - first_positive_idx, last_negative_idx + 1)
