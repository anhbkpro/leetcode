from lc_403_frog_jump import Solution


def test_can_cross():
    assert Solution.canCross([0, 1, 3, 5, 6, 8, 12, 17]) is True
    assert Solution.canCross([0, 1, 2, 3, 4, 8, 9, 11]) is False
