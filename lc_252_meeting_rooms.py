from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    if len(intervals) <= 1:
        return True

    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


class Solution:
    pass
