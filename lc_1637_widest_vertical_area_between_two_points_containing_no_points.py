from typing import List


class Solution:
    @staticmethod
    def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
        points_sorted = sorted(points, key=lambda x: x[0])
        max_width = points_sorted[1][0] - points_sorted[0][0]
        for i in range(2, len(points_sorted) - 1):
            if max_width < points_sorted[i + 1][0] - points_sorted[i][0]:
                max_width = points_sorted[i + 1][0] - points_sorted[i][0]
        return max_width
