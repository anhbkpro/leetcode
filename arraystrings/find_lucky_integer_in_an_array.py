from typing import Counter, List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for k, v in cnt.items():
            if k == v:
                ans = max(ans, k)

        return ans
