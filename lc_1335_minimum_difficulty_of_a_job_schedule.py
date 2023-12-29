from functools import cache
from typing import List


class Solution:
    @staticmethod
    def minDifficulty(jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # Initialize the min_diff matrix to record the minimum difficulty
        # of the job schedule
        min_diff = [[float('inf')] * n + [0] for i in range(d + 1)]
        for days_remaining in range(1, d + 1):
            for i in range(n - days_remaining + 1):
                daily_max_job_diff = 0
                for j in range(i + 1, n - days_remaining + 2):
                    # Use daily_max_job_diff to record maximum job difficulty
                    daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j - 1])
                    min_diff[days_remaining][i] = min(min_diff[days_remaining][i],
                                                      daily_max_job_diff + min_diff[days_remaining - 1][j])
        if min_diff[d][0] == float('inf'):
            return -1
        return min_diff[d][0]

    @staticmethod
    def minDifficultyTopDown(jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # Edge case: make sure there is at least one job per day
        if n < d:
            return -1

        # Precompute the maximum job difficulty for remaining jobs
        max_job_remaining = jobDifficulty[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])

        # Use memoization to avoid repeated computation of min_diff states
        @cache
        def min_diff(i, days_remaining):
            # Base case: finish all remaining jobs in the last day
            if days_remaining == 1:
                return max_job_remaining[i]

            res = float('inf')
            daily_max_job_diff = 0  # keep track of the maximum difficulty for today

            # Iterate through possible starting index for the next day
            # and ensure we have at least one job for each remaining day.
            for j in range(i, n - days_remaining + 1):
                daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j])
                res = min(res, daily_max_job_diff + min_diff(j + 1, days_remaining - 1))

            return res

        return min_diff(0, d)
