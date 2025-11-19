from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr, one_ptr = 0, 0
        while one_ptr < len(nums) and zero_ptr < len(nums):
            while one_ptr < len(nums) and nums[one_ptr] == 0:
                one_ptr += 1
            while zero_ptr < len(nums) and nums[zero_ptr] != 0:
                zero_ptr += 1

            if one_ptr < len(nums) and zero_ptr < len(nums):
                if one_ptr > zero_ptr:
                    nums[zero_ptr], nums[one_ptr] = nums[one_ptr], nums[zero_ptr]
                    zero_ptr += 1
                one_ptr += 1
