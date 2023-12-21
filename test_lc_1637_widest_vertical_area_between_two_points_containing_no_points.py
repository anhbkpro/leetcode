from lc_1637_widest_vertical_area_between_two_points_containing_no_points import Solution


def test_max_width_of_vertical_area():
    assert Solution.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
    assert Solution.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3
