from lc_867_transpose_matrix import Solution


def test_transpose():
    assert Solution.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
