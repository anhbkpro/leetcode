from lc_746_min_cost_climbing_stairs_bottom_up import Solution


def test_min_cost_climbing_stairs():
    assert Solution.minCostClimbingStairs(cost=[10, 15, 20]) == 15
    assert Solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
