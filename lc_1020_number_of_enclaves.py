from typing import List


def numEnclaves(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            # if it is a land, and it is on the border
            if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and grid[row][col] == 1:
                dfs(grid, row, col)
    return sum(sum(row) for row in grid)


def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        return
    # mark as visited
    grid[row][col] = 0
    # explore neighbors
    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)


class Solution:
    pass
