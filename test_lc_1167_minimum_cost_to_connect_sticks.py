from lc_1167_minimum_cost_to_connect_sticks import Solution


def test_connect_sticks():
    assert Solution.connectSticks([2, 4, 3]) == 14
    assert Solution.connectSticks([1, 8, 3, 5]) == 30
