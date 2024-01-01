from typing import List


class Solution:
    @staticmethod
    def findContentChildren(g: List[int], s: List[int]) -> int:
        i = j = 0
        g.sort()
        s.sort()
        ans = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1

        return ans
