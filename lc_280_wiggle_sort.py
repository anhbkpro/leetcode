from typing import List


def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i % 2 == 1 and i + 1 < n:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


class Solution:
    pass
