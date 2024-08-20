from minimum_moves_to_get_a_peaceful_board import Solution


def test_min_moves():
    assert Solution().minMoves([[0, 0], [1, 0], [1, 1]]) == 3
    assert Solution().minMoves([[0, 0], [0, 1], [0, 2], [0, 3]]) == 6
