from collections import Counter


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        f = Counter(s)
        ele = next((item for item in f if f[item] == 1), None)
        if not ele:
            return -1

        for i in range(len(s)):
            if s[i] == ele:
                return i

        return -1
