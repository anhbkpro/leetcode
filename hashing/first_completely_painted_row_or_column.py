from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        cols = [0] * n
        num_to_pos = {}
        for r in range(m):
            for c in range(n):
                num_to_pos[mat[r][c]] = (r, c)

        for i, num in enumerate(arr):
            r, c = num_to_pos[num]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i

        return -1
