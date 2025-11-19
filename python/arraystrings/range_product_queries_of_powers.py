from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        bins, rep = [], 1
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2

        ans = []
        for left, right in queries:
            cur = 1
            for i in range(left, right + 1):
                cur = cur * bins[i] % MOD
            ans.append(cur)
        return ans
