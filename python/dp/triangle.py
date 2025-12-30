from copy import copy
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        m = len(triangle)

        for r in range(m - 2, -1, -1):
            dp_tmp = copy.deepcopy(dp)
            for c in range(r + 1):  # At row r, we have (r + 1) columns
                dp_tmp[c] = triangle[r][c] + min(
                    dp_tmp[c], dp_tmp[min(c + 1, len(dp_tmp) + 1)]
                )

            dp = dp_tmp
        return dp[0]
