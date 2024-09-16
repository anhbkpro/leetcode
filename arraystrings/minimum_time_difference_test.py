from .minimum_time_difference import Solution


def test_minimum_time_difference():
    assert Solution().findMinDifference(["23:59", "00:00"]) == 1
    assert Solution().findMinDifference(["00:00", "23:59", "00:00"]) == 0
