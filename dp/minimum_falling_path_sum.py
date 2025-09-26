from copy import copy
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[-1]
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m - 2, -1, -1):
            dp_temp = copy.deepcopy(dp)

            for c in range(n):
                dp_temp[c] = matrix[r][c] + min(
                    dp[max(0, c - 1)], dp[c], dp[min(c + 1, n - 1)]
                )
            dp = dp_temp

        return min(dp)
