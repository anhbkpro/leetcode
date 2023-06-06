from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    ans = 0
    prev = 0
    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            # Overlap
            ans += 1
            if intervals[prev][1] > intervals[i][1]:
                prev = i
        else:
            prev = i
    return ans


class Solution:
    pass
