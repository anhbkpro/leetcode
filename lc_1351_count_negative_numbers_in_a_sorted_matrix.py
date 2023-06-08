from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    cols = len(grid[0])
    last_negative = cols - 1
    answer = 0
    for row in grid:
        if row[0] < 0:
            answer += cols
            continue

        if row[cols - 1] >= 0:
            continue
        # Using binary search find the index
        # which has the first negative element.
        lo, hi = 0, last_negative
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if row[mid] < 0:
                hi = mid - 1
            else:
                lo = mid + 1

        answer += cols - lo
        last_negative = lo
    return answer


class Solution:
    pass
