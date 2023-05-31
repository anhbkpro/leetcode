from typing import List


def maximizeSum(nums: List[int], k: int):
    max_item = max(nums)
    max_sum = 0
    for i in range(k):
        max_sum += max_item + i
    return max_sum


class Solution:
    pass
