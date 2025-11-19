from typing import List, Tuple


class Solution:
    def __init__(self):
        self.DIRECTIONS: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def regionsBySlashes(self, grid: List[str]) -> int:
        expanded_grid = self._build_cell3x3_grid(grid)
        number_of_regions = 0
        grid_size = len(expanded_grid)
        for r in range(grid_size):
            for c in range(grid_size):
                if expanded_grid[r][c] == 0:
                    number_of_regions += 1
                    self._dfs(expanded_grid, r, c)
        return number_of_regions

    def _build_cell3x3_grid(self, grid: List[str]) -> List[str]:
        grid_size = len(grid)
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]
        for r in range(grid_size):
            for c in range(grid_size):
                base_row = 3 * r
                base_col = 3 * c
                if grid[r][c] == "/":
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1
                elif grid[r][c] == "\\":
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1

        return expanded_grid

    def _dfs(self, grid: List[List[int]], row, col: int):
        if not self._is_valid_cell(grid, row, col):
            return

        self._mark_cell_as_visited(grid, row, col)
        self._explore_neighbors(grid, row, col)

    def _is_valid_cell(self, grid: List[List[int]], row: int, col: int) -> bool:
        return self._is_within_grid_bounds(grid, row, col) and self._is_cell_empty(
            grid, row, col
        )

    def _mark_cell_as_visited(self, grid: List[List[int]], row: int, col: int) -> None:
        grid[row][col] = 1

    def _is_within_grid_bounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        """
        Check if the given row and column are within the bounds of the grid.

        Parameters:
            grid (List[List[int]]): The grid to check bounds within.
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if the row and column are within the grid bounds, False otherwise.
        """
        grid_size = len(grid)
        return 0 <= row < grid_size and 0 <= col < grid_size

    def _is_cell_empty(self, grid: List[List[int]], row: int, col: int) -> bool:
        return grid[row][col] == 0

    def _explore_neighbors(self, grid: List[List[int]], row: int, col: int) -> None:
        for dx, dy in self.DIRECTIONS:
            new_row, new_col = row + dx, col + dy
            self._dfs(grid, new_row, new_col)
