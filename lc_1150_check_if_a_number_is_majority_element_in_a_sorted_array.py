from typing import List


def isMajorityElement(nums: List[int], target: int) -> bool:
    return nums.count(target) > len(nums) // 2


class Solution:
    pass
