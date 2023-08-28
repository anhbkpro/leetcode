from lc_223_rectangle_area import Solution


def test_compute_area():
    assert Solution.compute_area(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert Solution.compute_area(-2, -2, 2, 2, -2, -2, 2, 2) == 16
