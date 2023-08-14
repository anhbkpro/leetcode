from typing import List


class Solution:
    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n

        for r in range(m):
            for c in range(n):
                if c == 0 and r == 0:
                    dp[c] = grid[r][c]
                    continue

                if c == 0 or r == 0:
                    dp[c] = grid[r][c] + dp[max(0, c - 1)]
                    continue

                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]
