from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
    return True


class Solution:
    pass


