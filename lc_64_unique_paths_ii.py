from typing import List


def uniquePathsWithObstacles(obstacle_grid: List[List[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [0] * n
    dp[n - 1] = 1
    for row in reversed(range(m)):
        for col in reversed(range(n)):
            if obstacle_grid[row][col] == 1:
                dp[col] = 0
            elif col < n - 1:
                dp[col] = dp[col] + dp[col + 1]
    return dp[0]


class Solution:
    pass
