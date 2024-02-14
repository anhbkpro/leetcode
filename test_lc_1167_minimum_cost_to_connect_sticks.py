from lc_1167_minimum_cost_to_connect_sticks import Solution


def test_connect_sticks():
    assert Solution.connect_sticks([2, 4, 3]) == 14
    assert Solution.connect_sticks([1, 8, 3, 5]) == 30
    assert Solution.connect_sticks([5]) == 0
