from lc_55_jump_game import Solution


def test_can_jump():
    assert Solution.canJump(nums=[2, 3, 1, 1, 4]) is True
    assert Solution.canJump(nums=[3, 2, 1, 0, 4]) is False
