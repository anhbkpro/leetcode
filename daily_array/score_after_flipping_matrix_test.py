from daily_array.score_after_flipping_matrix import Solution


def test_matrix_score():
    assert Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
    assert Solution().matrixScore([[0]]) == 1
