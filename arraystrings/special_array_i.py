from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        check = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == check:
                return False
            check = not check

        return True
