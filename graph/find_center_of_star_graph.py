from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = {}
        for u, v in edges:
            if u in freq:
                return u
            if v in freq:
                return v
            freq[u] = True
            freq[v] = True

        return -1
