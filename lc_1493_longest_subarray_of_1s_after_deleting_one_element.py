from typing import List


def longestSubarray(nums: List[int]) -> int:
    lo, hi = 0, 0
    zero_count = 0
    ans = 0

    while hi < len(nums):
        zero_count += (nums[hi] == 0)
        while zero_count > 1:
            zero_count -= (nums[lo] == 0)
            lo += 1
        ans = max(ans, hi - lo)
        hi += 1

    return ans


class Solution:
    pass
