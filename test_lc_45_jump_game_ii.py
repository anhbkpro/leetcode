from lc_45_jump_game_ii import Solution


def test_jump():
    assert Solution.jump([2, 3, 1, 1, 4]) == 2
    assert Solution.jump([2, 3, 0, 1, 4]) == 2
