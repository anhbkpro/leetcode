from lc_1870_minimum_speed_to_arrive_on_time import Solution


def test_min_speed_on_time():
    assert Solution.min_speed_on_time(dist=[1, 3, 2], hour=6) == 1
    assert Solution.min_speed_on_time(dist=[1, 3, 2], hour=2.7) == 3
    assert Solution.min_speed_on_time(dist=[1, 3, 2], hour=1.9) == -1
