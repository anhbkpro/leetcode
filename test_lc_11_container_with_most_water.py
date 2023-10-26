from lc_11_container_with_most_water import Solution


def test_max_area():
    assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution.maxArea(height=[1, 1]) == 1
