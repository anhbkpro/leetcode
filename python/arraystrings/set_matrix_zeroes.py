from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        R = len(matrix)
        C = len(matrix[0])
        rows = set()
        cols = set()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(R):
            for c in range(C):
                if r in rows or c in cols:
                    matrix[r][c] = 0
