from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for k, v in c.items():
            ans += v if v % 2 == 0 else (v - 1)

        return min(ans + 1, len(s))
