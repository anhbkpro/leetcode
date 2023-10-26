from lc_42_trapping_rain_water import Solution


def test_trapping_rain_water():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert Solution.trap(height) == 6

    height = [4, 2, 0, 3, 2, 5]
    assert Solution.trap(height) == 9

    height = [4, 2, 3]
    assert Solution.trap(height) == 1

    height = [4, 2]
    assert Solution.trap(height) == 0
