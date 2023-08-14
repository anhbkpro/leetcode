from lc_931_minimum_falling_path_sum import Solution


def test_min_falling_path_sum():
    assert Solution.min_falling_path_sum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert Solution.min_falling_path_sum(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 12
    assert Solution.min_falling_path_sum(matrix=[[1, 2], [1, 1]]) == 2
