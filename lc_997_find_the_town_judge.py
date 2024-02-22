from typing import List


class Solution:
    @staticmethod
    def find_judge(n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)
        for f, s in trust:
            in_degrees[s] += 1
            out_degrees[f] += 1

        for i in range(1, n + 1):
            # everyone trusts the judge and the judge trusts no one
            if in_degrees[i] == n - 1 and out_degrees[i] == 0:
                return i

        return -1
