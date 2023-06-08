from lc_1351_count_negative_numbers_in_a_sorted_matrix import countNegatives


def test_count_negatives():
    assert countNegatives([[1, -1], [-1, -1]]) == 3
    assert countNegatives([[3, 2], [1, 0]]) == 0
    assert countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
