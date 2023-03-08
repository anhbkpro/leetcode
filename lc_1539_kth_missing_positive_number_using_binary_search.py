from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] - mid - 1 < k:
            left = mid + 1
        else:
            right = mid - 1
    return left + k


class Solution:
    pass
