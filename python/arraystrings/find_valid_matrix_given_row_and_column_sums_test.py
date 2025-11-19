from .find_valid_matrix_given_row_and_column_sums import Solution


def test_restore_matrix():
    assert Solution().restoreMatrix([3, 8], [4, 7]) == [[3, 0], [1, 7]]
