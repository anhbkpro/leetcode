from lc_119_pascals_triangle_ii import Solution


def test_get_row():
    assert Solution().getRow(rowIndex=3) == [1, 3, 3, 1]
    assert Solution().getRow(rowIndex=0) == [1]
