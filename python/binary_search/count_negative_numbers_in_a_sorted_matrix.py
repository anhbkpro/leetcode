from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        last_negative = cols - 1
        answer = 0
        for row in range(rows):
            if grid[row][0] < 0:
                answer += cols
                continue

            if grid[row][cols - 1] >= 0:
                continue

            lo, hi = 0, last_negative
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if grid[row][mid] < 0:
                    hi = mid - 1
                else:
                    lo = mid + 1

            answer += cols - lo
            last_negative = lo
        return answer
