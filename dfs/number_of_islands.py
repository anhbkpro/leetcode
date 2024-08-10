from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num_islands += 1
                    self._dfs(grid, r, c)

        return num_islands

    def _dfs(self, grid, r, c):
        """
        Start exploring the island from the current cell.
        """
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            # We are out of the grid or we reached water, so we can safely return
            return

        # Mark as visited, this will prevent us from visiting it again in the future
        grid[r][c] = "0"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            # Visit all the neighbors
            self._dfs(grid, r + dr, c + dc)
