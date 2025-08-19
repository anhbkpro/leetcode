from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = -1
        for right in range(len(nums)):
            if nums[right] != 0:
                left = right
            ans += right - left

        return ans