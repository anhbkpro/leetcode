from typing import List


class SolutionDFS:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _check_in_bound(self, grid: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def _dfs(self, grid: List[List[str]], row: int, col: int, visited):
        if (
            (row, col) in visited
            or not self._check_in_bound(grid, row, col)
            or grid[row][col] != "1"
        ):
            return

        visited.add((row, col))
        for x, y in self.dirs:
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


class SolutionBFS:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _check_in_bound(self, grid: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    q = [(row, col)]
                    while q:
                        r, c = q.pop()
                        visited.add((r, c))
                        for x, y in self.dirs:
                            next_row, next_col = r + x, c + y
                            if (
                                self._check_in_bound(grid, next_row, next_col)
                                and (next_row, next_col) not in visited
                                and grid[next_row][next_col] == "1"
                            ):
                                q.append((next_row, next_col))
                                visited.add((next_row, next_col))

        return num_islands
