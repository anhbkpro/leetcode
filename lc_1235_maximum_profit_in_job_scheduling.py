from bisect import bisect_right
from typing import List


def job_scheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    # Sort by start time
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
    dp = [-1] * (n + 1)

    start_time = [startTime for startTime, endTime, profit in jobs]

    def dfs(cur_index):
        if cur_index == n:
            return 0

        if dp[cur_index] != -1:
            return dp[cur_index]

        skip_job = dfs(cur_index + 1)
        next_index = bisect_right(start_time, jobs[cur_index][1] - 1)
        do_job = jobs[cur_index][2] + dfs(next_index)
        dp[cur_index] = max(do_job, skip_job)
        return dp[cur_index]

    return dfs(0)


class Solution:
    pass
