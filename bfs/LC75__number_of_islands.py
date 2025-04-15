from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    self.bfs(grid, r, c)

        return island_count

    def bfs(self, grid, row, col):
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        grid[row][col] = "0"  # Mark as visited
        q = deque([(row, col)])

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                if (
                    0 <= next_r < len(grid)
                    and 0 <= next_c < len(grid[0])
                    and grid[next_r][next_c] == "1"
                ):
                    grid[next_r][next_c] = "0"  # Mark as visited
                    q.append((next_r, next_c))
