class Solution:
    @staticmethod
    def longest_palindrome_subseq(s: str) -> int:
        n = len(s)
        dp = [0] * n
        # The other array dpPrev is important to understand. It helps us by
        # remembering the previous state that we completed previously.
        # dpPrev[j] stores the length of the longest palindromic subsequence
        # of the substring from index i + 1 to j in s.
        # It is analogous to dp[i + 1][j] in the previous approach.
        dp_prev = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = dp_prev[j - 1] + 2
                else:
                    dp[j] = max(dp_prev[j], dp[j - 1])
            dp_prev = dp[:]  # Copy dp to dp_prev same as copy.deepcopy(dp)

        return dp[n - 1]
