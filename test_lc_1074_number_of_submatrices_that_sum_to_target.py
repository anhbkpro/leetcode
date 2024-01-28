from lc_1074_number_of_submatrices_that_sum_to_target import Solution


def test_num_submatrix_sum_target():
    assert Solution.numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4
