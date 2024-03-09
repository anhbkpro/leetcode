from typing import List


class Solution:
    @staticmethod
    def get_common(nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return -1

        def binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        for num in nums1:
            if binary_search(nums2, num) != -1:
                return num

        return -1

    @staticmethod
    def get_common_two_pointers(nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return -1
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
