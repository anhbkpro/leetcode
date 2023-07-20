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


def missing_number_binary_search(arr: List[int]) -> int:
    n = len(arr)
    step = (arr[-1] - arr[0]) // n
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[0] + mid * step:
            left = mid + 1
        else:
            right = mid

    return arr[0] + left * step


class Solution:
    pass
