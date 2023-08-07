from lc_74_search_a_2d_matrix import Solution


def test_search_matrix():
    assert Solution.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert Solution.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert Solution.search_matrix_lc([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert Solution.search_matrix_lc([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False