import collections


class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return Solution.findTheDifference(t, s)

        sm = collections.Counter(s)
        tm = collections.Counter(t)

        for k in sm:
            if k not in tm or sm[k] != tm[k]:
                return k

        return ""

    @staticmethod
    def findTheDifference2(s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
