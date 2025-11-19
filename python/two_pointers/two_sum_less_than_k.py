from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi, max_sum = 0, len(nums) - 1, -1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum < k:
                max_sum = max(max_sum, sum)
                lo += 1
            else:
                hi -= 1
        return max_sum
