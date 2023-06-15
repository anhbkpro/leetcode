from typing import List


def is_majority_element_bs(nums: List[int], target: int) -> bool:
    first_index = lower_bound(nums, target)
    last_index = first_index + len(nums) // 2
    return last_index < len(nums) and nums[last_index] == target


def lower_bound(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


class Solution:
    pass
