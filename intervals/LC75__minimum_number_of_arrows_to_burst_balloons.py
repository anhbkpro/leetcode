from typing import List


class SolutionSortByStart:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort the points by the start point
        points.sort(key=lambda x: x[0])
        number_of_arrows = 0
        intervals = []
        for start, end in points:
            if intervals and start <= intervals[-1][-1]:
                # shrink the end to build the common interval
                intervals[-1][-1] = min(intervals[-1][-1], end)
            else:
                intervals.append([start, end])
                number_of_arrows += 1

        return number_of_arrows


# Better solution, sort by end point
class SolutionSortByEnd:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by end point for optimal greedy approach
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points[1:]:
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows
