from typing import List


def missing_number(arr: List[int]) -> int:
    n = len(arr)
    step = (arr[-1] - arr[0]) // n

    for i in range(n):
        if arr[i] != arr[0] + i * step:
            return arr[0] + i * step

    return arr[0]


class Solution:
    pass
