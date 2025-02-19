from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p_left, p_right = 0, len(nums) - 1
        operations = 0
        while p_left < p_right:
            if nums[p_left] + nums[p_right] == k:
                p_left += 1
                p_right -= 1
                operations += 1
            elif nums[p_left] + nums[p_right] > k:
                p_right -= 1
            else:
                p_left += 1

        return operations
