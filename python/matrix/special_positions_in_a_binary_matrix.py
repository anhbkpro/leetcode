from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        r = [0] * m
        c = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 1:
                    continue

                if r[i] == 1 and c[j] == 1:
                    ans += 1

        return ans
