from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n  # Create an array to store maximum points at each position
        dp[-1] = questions[-1][0]  # Base case: last question's points

        for i in range(n - 2, -1, -1):  # Iterate from second-to-last question to first
            dp[i] = questions[i][0]  # Start with points from solving this question
            skip = questions[i][1]  # How many questions to skip if we solve this one
            if (
                i + skip + 1 < n
            ):  # If we can still solve another question after skipping
                dp[i] += dp[i + skip + 1]  # Add max points from that future position

            # dp[i] = max(solve it, skip it)
            dp[i] = max(dp[i], dp[i + 1])  # Choose the maximum of solving or skipping

        return dp[0]  # Return the maximum points from the first question
