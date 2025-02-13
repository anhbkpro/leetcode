from typing import List


class Solution:
    def _check_in_bound(self, grid: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def _dfs(self, grid: List[List[str]], row: int, col: int, visited):
        if (row, col) in visited or not self._check_in_bound(grid, row, col) or grid[row][col] != "1":
            return

        visited.add((row, col))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in dirs:
            next_row, next_col = row + x, col + y
            self._dfs(grid, next_row, next_col, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    self._dfs(grid, row, col, visited)

        return num_islands