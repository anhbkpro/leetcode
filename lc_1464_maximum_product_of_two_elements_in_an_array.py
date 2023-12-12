from typing import List


class Solution:
    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            ans = max(ans, (nums[l] - 1) * (nums[r] - 1))
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return ans
