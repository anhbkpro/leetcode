from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        first_index = findBound(nums, target, True)
        if first_index == -1:
            return [-1, -1]
        second_index = findBound(nums, target, False)

        return [first_index, second_index]


def findBound(nums: List[int], target: int, is_first: bool) -> int:
    n = len(nums) - 1
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if is_first:
                if mid == lo or nums[mid - 1] < target:
                    return mid

                hi = mid - 1
            else:
                if mid == hi or nums[mid + 1] > target:
                    return mid

                lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1
