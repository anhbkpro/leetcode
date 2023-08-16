class Solution:
    @staticmethod
    def longest_palindrome_subseq(s: str) -> int:
        n = len(s)
        memo = [[0] * n for _ in range(n)]

        def lps(i: int, j: int) -> int:
            if memo[i][j] != 0:
                return memo[i][j]
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                memo[i][j] = 2 + lps(i + 1, j - 1)
            else:
                memo[i][j] = max(lps(i, j - 1), lps(i + 1, j))

            return memo[i][j]

        return lps(0, n - 1)
