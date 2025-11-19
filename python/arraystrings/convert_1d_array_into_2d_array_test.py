from .convert_1d_array_into_2d_array import Solution


def test_construct_2d_array():
    assert Solution().construct2DArray([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]]
    assert Solution().construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]]
    assert Solution().construct2DArray([1, 2], 1, 1) == []
