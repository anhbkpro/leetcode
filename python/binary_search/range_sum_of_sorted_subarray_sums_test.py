from .range_sum_of_sorted_subarray_sums import Solution


def test_range_sum_of_sorted_subarray_sums():
    assert Solution().rangeSum([1, 2, 3, 4], 4, 1, 5) == 13
