from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        if sum_chalk % k == 0 or k % sum_chalk == 0:
            return 0

        remaining = k % sum_chalk
        for i, c in enumerate(chalk):
            if remaining < c:
                return i

            remaining -= c

        return 0
