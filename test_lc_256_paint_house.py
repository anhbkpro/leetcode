from lc_256_paint_house import min_cost


def test_min_cost():
    assert min_cost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]) is 10
    assert min_cost(costs=[]) is 0
    assert min_cost(costs=[[7, 6, 2]]) is 2
