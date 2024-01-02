from lc_2610_convert_an_array_into_a_2d_array_with_conditions import Solution


def test_find_matrix():
    assert Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]) == [[1, 3, 4, 2], [1, 3], [1]]
