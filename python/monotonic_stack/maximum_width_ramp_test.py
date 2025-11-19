from .maximum_width_ramp import Solution


def test_maximum_width_ramp():
    assert Solution().maxWidthRamp(nums=[6, 0, 8, 2, 1, 5]) == 4
    assert Solution().maxWidthRamp(nums=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
