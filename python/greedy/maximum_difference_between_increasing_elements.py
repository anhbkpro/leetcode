from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        ans = -1
        for i in range(1, len(nums)):
            num = nums[i]
            if min_num < num:
                ans = max(ans, num - min_num)
            else:
                min_num = num
        return ans
