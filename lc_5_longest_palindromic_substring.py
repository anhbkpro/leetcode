class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        n = len(s)
        # dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        # diff = 0
        for i in range(n):
            dp[i][i] = True

        # diff = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # diff >= 2 -> n
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]
