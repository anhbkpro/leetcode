from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    sum_of_current_window = 0
    res = float('inf')

    while right < len(nums):
        sum_of_current_window += nums[right]

        while sum_of_current_window >= target:
            res = min(res, right - left + 1)
            sum_of_current_window -= nums[left]
            left += 1

        right += 1

    return res if res != float('inf') else 0


class Solution:
    pass
