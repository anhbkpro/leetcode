from typing import List


def longest_subsequence(arr: List[int], difference: int) -> int:
    dp = {}
    answer = 1
    for a in arr:
        # Input: arr = [1,5,7,8,5,[3],4,2,1], difference = -2
        # what is the length of the arithmetic sequence ending in 3?
        # it depends on the length of the sequence ending in 5 on the left side of 3.
        # which depends on the length of the sequence ending in 7 on the left side of 5.
        # a = 1 => before_a = dp.get( 3, 0)  = 0 => dp[1] = 1
        # a = 5 => before_a = dp.get( 7, 0)  = 0 => dp[5] = 1
        # a = 7 => before_a = dp.get( 9, 0)  = 0 => dp[7] = 1
        # a = 8 => before_a = dp.get(10, 0)  = 0 => dp[8] = 1
        # a = 5 => before_a = dp.get( 7, 0)  = 1 => dp[5] = 1 + 1 = 2 => max = 2
        # a = 3 => before_a = dp.get( 5, 0)  = 2 => dp[3] = 2 + 1 = 3 => max = 3
        # a = 4 => before_a = dp.get( 6, 0)  = 0 => dp[4] = 1
        # a = 2 => before_a = dp.get( 4, 0)  = 1 => dp[4] = 1 + 1 = 2 => max = 3
        # a = 1 => before_a = dp.get( 3, 0)  = 3 => dp[1] = 3 + 1 = 4 => max = 4
        before_a = dp.get(a - difference, 0)
        dp[a] = before_a + 1
        answer = max(answer, dp[a])

    return answer


class Solution:
    pass
