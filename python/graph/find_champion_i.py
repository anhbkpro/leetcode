from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        candidates = set([i for i in range(C)])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    if c in candidates:
                        candidates.remove(c)

        if len(candidates) != 1:
            return -1

        return list(candidates)[0]
