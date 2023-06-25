import sys
from typing import List


def smallestCommonElement(mat: List[List[int]]) -> int:
    common_hash = set(mat[0])
    for row in mat[1:]:
        common_hash &= set(row)

    ans = sys.maxsize
    for item in common_hash:
        if item < ans:
            ans = item

    if ans == sys.maxsize:
        return -1

    return ans


class Solution:
    pass
