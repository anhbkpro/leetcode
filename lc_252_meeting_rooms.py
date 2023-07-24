from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True


class Solution:
    pass
