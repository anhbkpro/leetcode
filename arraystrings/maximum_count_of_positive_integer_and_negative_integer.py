from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = len([num for num in nums if num < 0])
        positive_count = len([num for num in nums if num > 0])
        return max(negative_count, positive_count)


class OnePassSolution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = 0
        positive_count = 0
        for num in nums:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
        return max(negative_count, positive_count)


class BinarySearchSolution:
    def _binary_search(self, nums: List[int], target: int, find_left: bool) -> int:
        """
        Generic binary search helper that can find either left or right boundary.
        Args:
            nums: Input array
            target: Target value to compare against (0)
            find_left: If True, finds leftmost boundary, otherwise rightmost
        Returns:
            Index of the boundary
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if find_left:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return right if find_left else left

    def maximumCount(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Sort the array first since binary search requires sorted input
        nums = sorted(nums)

        # Handle edge cases of all positive/negative numbers
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)

        # Find boundaries of negative and positive numbers
        last_negative = self._binary_search(nums, 0, True)
        first_positive = self._binary_search(nums, 0, False)

        negative_count = last_negative + 1
        positive_count = len(nums) - first_positive

        return max(negative_count, positive_count)
