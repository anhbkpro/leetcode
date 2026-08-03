class Solution:
    def stoneGameIII(self, A):
        dp = [0] * 3

        for i in range(len(A) - 1, -1, -1):
            dp[i % 3] = max(
                sum(A[i:i + k]) - dp[(i + k) % 3]
                for k in range(1, min(3, len(A) - i) + 1)
            )

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
