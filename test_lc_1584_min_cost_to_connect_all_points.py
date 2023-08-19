from lc_1584_min_cost_to_connect_all_points import Solution


def test_min_cost_connect_points():
    assert Solution.minCostConnectPoints(
        points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    ) == 20
    assert Solution.minCostConnectPoints(
        points=[[3, 12], [-2, 5], [-4, 1]]
    ) == 18
