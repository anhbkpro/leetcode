from .maximum_matrix_sum import Solution


def test_max_matrix_sum():
    assert Solution().maxMatrixSum(matrix=[[1, -1], [-1, 1]]) == 4
    assert Solution().maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
