from lc_1727_largest_submatrix_with_rearrangements import Solution


def test_largest_submatrix():
    assert Solution.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert Solution.largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]) == 3
