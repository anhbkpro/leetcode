from lc_1197_minimum_knight_moves import Solution


def test_min_knight_moves():
    assert Solution().minKnightMoves(x=2, y=1) == 1
    assert Solution().minKnightMoves(x=5, y=5) == 4
