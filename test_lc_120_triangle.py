from lc_120_triangle import Solution


def test_minimum_total():
    assert Solution.minimum_total(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution.minimum_total(triangle=[[-10]]) == -10
