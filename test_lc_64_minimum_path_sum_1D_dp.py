from lc_64_minimum_path_sum_1D_dp import Solution


def test_min_path_sum():
    assert Solution.min_path_sum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution.min_path_sum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
    assert Solution.min_path_sum(grid=[[1, 2], [1, 1]]) == 3
