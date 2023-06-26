from typing import List


def removeInterval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    remove_start, remove_end = toBeRemoved
    ans = []

    for start, end in intervals:
        if start >= remove_start and end <= remove_end:
            continue

        if start >= remove_end or end <= remove_start:
            ans.append([start, end])
        else:
            if start < remove_start:
                ans.append([start, remove_start])
            if end > remove_end:
                ans.append([remove_end, end])

    return ans


class Solution:
    pass
