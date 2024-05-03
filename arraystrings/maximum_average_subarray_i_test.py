from arraystrings.maximum_average_subarray_i import Solution


def test_maximum_average_subarray():
    assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert Solution().findMaxAverage([5], 1) == 5.0
