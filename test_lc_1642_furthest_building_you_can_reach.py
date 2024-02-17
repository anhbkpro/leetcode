from lc_1642_furthest_building_you_can_reach import Solution


def test_furthest_building():
    assert Solution.furthest_building(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
    assert Solution.furthest_building(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
