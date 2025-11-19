from typing import List


class Solution:
    def find_max(self, grid: List[List[int]], row: int, col: int) -> int:
        max_element = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                max_element = max(max_element, grid[i][j])

        return max_element

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        print(max_local)
        for i in range(n - 2):
            for j in range(n - 2):
                max_local[i][j] = self.find_max(grid, i, j)

        return max_local
