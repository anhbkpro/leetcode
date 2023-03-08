from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    i = 0
    for num in range(1, arr[-1] + k + 1):
        if i < len(arr) and num == arr[i]:
            i += 1
        else:
            k -= 1
            if k == 0:
                return num


class Solution:
    pass
