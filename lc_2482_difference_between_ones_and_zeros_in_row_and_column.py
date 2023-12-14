from typing import List


class Solution:
    @staticmethod
    def onesMinusZeros(grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        onesRow = [0] * R
        onesCol = [0] * C

        for i in range(R):
            for j in range(C):
                onesRow[i] += grid[i][j]
                onesCol[j] += grid[i][j]
        diff = []
        for i in range(R):
            temp = []
            for j in range(C):
                temp.append(2 * onesRow[i] + 2 * onesCol[j] - R - C)
            diff.append(temp)
        print(diff)

        return diff
