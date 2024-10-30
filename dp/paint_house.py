from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        for i in range(1, len(costs)):
            # Total cost of painting ith house red.
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            # Total cost of painting ith house green.
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            # Total cost of painting ith house blue.
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])
