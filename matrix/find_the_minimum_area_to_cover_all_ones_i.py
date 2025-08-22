from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minx, miny = float("inf"), float("inf")
        maxx, maxy = -1, -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    minx = min(minx, i)
                    maxx = max(maxx, i)
                    miny = min(miny, j)
                    maxy = max(maxy, j)

        if minx == float("inf") or miny == float("inf") or maxx == -1 or maxy == -1:
            return 0
        return (maxx - minx + 1) * (maxy - miny + 1)
