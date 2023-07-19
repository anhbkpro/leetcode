from math import inf
from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    ans = 0
    k = -inf
    for x, y in intervals:
        if x >= k:
            # Update end time
            k = y
        else:
            # Remove interval
            ans += 1

    return ans


class Solution:
    pass
