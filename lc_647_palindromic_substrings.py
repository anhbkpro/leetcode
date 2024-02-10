class Solution:
    @staticmethod
    def countSubstrings(s: str) -> int:
        def is_palindrome(s: str, lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False

                lo += 1
                hi -= 1

            return True

        ans = 0
        for lo in range(len(s)):
            for hi in range(lo, len(s)):
                ans += is_palindrome(s, lo, hi)

        return ans


    @staticmethod
    def count_substrings_dp(s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Base case for single letter strings
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case for double letter strings
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += dp[i][i + 1]

        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                dp[i][i + length - 1] = s[i] == s[i + length - 1] and dp[i + 1][i + length - 2]
                ans += dp[i][i + length - 1]

        return ans
