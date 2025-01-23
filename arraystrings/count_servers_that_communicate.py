from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        total_computers = 0 
        silo_computers = 0 
        rows, cols = len(grid), len(grid[0])
        row_computers = [0] * rows
        col_computers = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_computers[r] += 1
                    col_computers[c] += 1
                    total_computers += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_computers[r] > 1 or col_computers[c] > 1):
                    grid[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    silo_computers += 1

        return total_computers - silo_computers
