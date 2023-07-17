from bisect import bisect_right
from typing import List


def max_taxi_earnings(n: int, rides: List[List[int]]) -> int:
    rides.sort()
    n = len(rides)   # number of rides (overriding n)
    dp = [0] * n
    starts = [start for start, end, tip in rides]

    def dfs(cur_index):
        if cur_index == n:
            return 0

        if dp[cur_index] != 0:
            return dp[cur_index]

        skip_ride = dfs(cur_index + 1)
        next_index = bisect_right(starts, rides[cur_index][1] - 1)
        do_ride = rides[cur_index][1] - rides[cur_index][0] + rides[cur_index][2] + dfs(next_index)
        dp[cur_index] = max(do_ride, skip_ride)
        return dp[cur_index]

    return dfs(0)


class Solution:
    pass
