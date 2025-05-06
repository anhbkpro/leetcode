from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero = i
                break

        non_zero = first_zero
        for i in range(len(nums)):
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
            if non_zero < len(nums) and nums[i] == 0 and i < non_zero:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
