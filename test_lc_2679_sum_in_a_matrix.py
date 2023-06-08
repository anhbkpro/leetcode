from lc_2679_sum_in_a_matrix import matrix_sum


def test_matrix_sum():
    assert matrix_sum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]) == 15
    assert matrix_sum([[1]]) == 1
