from lc_1575_count_all_possible_routes_iterative import countRoutes


def test_count_routes():
    assert countRoutes([2, 3, 6, 8, 4], 1, 3, 5) == 4
    assert countRoutes([4, 3, 1], 1, 0, 6) == 5
