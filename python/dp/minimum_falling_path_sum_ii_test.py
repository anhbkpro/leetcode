from dp.minimum_falling_path_sum_ii import Solution


def test_min_falling_path_sum():
    assert Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    assert Solution().minFallingPathSum([[7]]) == 7
