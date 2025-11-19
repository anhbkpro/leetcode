from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        candidates = set([i for i in range(n)])
        for u, v in edges:
            if v in candidates:
                candidates.remove(v)

        if len(candidates) == 1:
            return list(candidates)[0]

        return -1
