from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort the points by the start point
        points.sort(key=lambda x: x[0])
        number_of_arrows = 0
        intervals = []
        for start, end in points:
            if not intervals:
                intervals.append([start, end])
                number_of_arrows += 1
                continue
            if start <= intervals[-1][-1]:
                # shrink the end to build the common interval
                intervals[-1][-1] = min(intervals[-1][-1], end)
            else:
                intervals.append([start, end])
                number_of_arrows += 1

        return number_of_arrows
