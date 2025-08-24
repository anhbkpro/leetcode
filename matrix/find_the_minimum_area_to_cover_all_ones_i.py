from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        minx, miny = n, m
        maxx, maxy = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    minx = min(minx, i)
                    maxx = max(maxx, i)
                    miny = min(miny, j)
                    maxy = max(maxy, j)

        return (maxx - minx + 1) * (maxy - miny + 1)
