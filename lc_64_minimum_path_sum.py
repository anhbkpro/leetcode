from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if c == 0 and r == 0:
                dp[r][c] = grid[r][c]
                continue

            if c == 0 or r == 0:
                dp[r][c] = grid[r][c] + dp[max(0, r - 1)][max(0, c - 1)]
                continue

            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

    return dp[-1][-1]


class Solution:
    pass
