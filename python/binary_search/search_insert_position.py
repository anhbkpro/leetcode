from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p_left, p_right = 0, len(nums) - 1

        # Handle target smaller than first element
        if target <= nums[0]:
            return 0

        while p_left <= p_right:
            p_mid = (p_left + p_right) // 2
            if nums[p_mid] == target:
                # Find leftmost position for duplicates
                while p_mid > 0 and nums[p_mid - 1] == target:
                    p_mid -= 1
                return p_mid
            if nums[p_mid] > target:
                p_right = p_mid - 1
            else:
                p_left = p_mid + 1

        return p_left
