from lc_1199_minimum_time_to_build_blocks import Solution


def test_min_build_time():
    assert Solution.minBuildTime(blocks=[1], split=1) == 1
    assert Solution.minBuildTime(blocks=[1, 2], split=5) == 7
    assert Solution.minBuildTime(blocks=[1, 2, 3], split=1) == 4
