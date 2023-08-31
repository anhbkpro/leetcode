from lc_1326_minimum_number_of_taps_to_open_to_water_a_garden import Solution


def test_min_taps():
    assert Solution.minTaps(5, [3, 4, 1, 1, 0, 0]) == 1
    assert Solution.minTaps(3, [0, 0, 0, 0]) == -1
