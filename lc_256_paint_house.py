from typing import List


def min_cost(costs: List[List[int]]) -> int:
    total_houses = len(costs)
    for i in range(1, total_houses):
        # Total cost of painting ith house red.
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        # Total cost of painting ith house green.
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        # Total cost of painting ith house blue.
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

    if len(costs) == 0:
        return 0

    return min(costs[-1])  # Return the minimum in the last row.
