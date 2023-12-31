from collections import defaultdict


class Solution:
    @staticmethod
    def maxLengthBetweenEqualCharacters(s: str) -> int:
        f = defaultdict()
        ans = -1
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]] = i
            else:
                ans = max(ans, i - f[s[i]] - 1)

        return ans
