from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.ROW = len(matrix)
        self.COL = len(matrix[0])
        max_area = 0
        dp = [[0] * self.COL for _ in range(self.ROW)]
        for r in range(self.ROW):
            for c in range(self.COL):
                if matrix[r][c] == "0":
                    continue

                # compute the maximum width and update dp with it
                width = dp[r][c] = dp[r][c - 1] + 1 if c else 1

                # compute the maximum area rectangle with a lower right corner at [r, c]
                for k in range(r, -1, -1):
                    width = min(width, dp[k][c])
                    max_area = max(max_area, width * (r - k + 1))
        return max_area
