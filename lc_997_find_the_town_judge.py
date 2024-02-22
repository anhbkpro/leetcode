from typing import List


class Solution:
    @staticmethod
    def find_judge(n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        indegrees = [0] * (n + 1)
        outdegrees = [0] * (n + 1)
        for f, s in trust:
            indegrees[s] += 1
            outdegrees[f] += 1

        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i

        return -1
