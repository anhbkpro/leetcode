from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:
        component = [0] * n
        comp_no = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp_no += 1
            component[i] = comp_no

        return [component[u] == component[v] for u, v in queries]
