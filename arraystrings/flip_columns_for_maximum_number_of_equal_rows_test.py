from .flip_columns_for_maximum_number_of_equal_rows import Solution


def test_max_equal_rows_after_flips():
    assert (
        Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]])
        == 1
    )
