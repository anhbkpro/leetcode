from lc_1064_fixed_point import Solution


def test_fixed_point():
    assert Solution().fixedPoint([-10, -5, 0, 3, 7]) == 3
    assert Solution().fixedPoint([0, 2, 5, 8, 17]) == 0
    assert Solution().fixedPoint([-10, -5, 3, 4, 7, 9]) == -1
