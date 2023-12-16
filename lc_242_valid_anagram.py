from collections import Counter


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)

        return sc == tc
