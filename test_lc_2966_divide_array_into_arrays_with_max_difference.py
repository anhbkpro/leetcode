from lc_2966_divide_array_into_arrays_with_max_difference import Solution


def test_divide_array():
    assert Solution.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
