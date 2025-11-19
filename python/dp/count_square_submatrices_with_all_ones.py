from typing import List


class Solution:
    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        right = self.solve(i, j + 1, grid, dp)
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, min(diagonal, below))
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += self.solve(i, j, matrix, dp)
        return ans


class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans += dp[i + 1][j + 1]
        return ans
