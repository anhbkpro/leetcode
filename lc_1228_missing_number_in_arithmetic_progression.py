from typing import List


def missing_number(arr: List[int]) -> int:
    n = len(arr)
    step = (arr[-1] - arr[0]) // n
    expected = arr[0]

    for val in arr:
        if val != expected:
            return expected
        expected += step

    return expected


class Solution:
    pass
