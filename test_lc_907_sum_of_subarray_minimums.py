from lc_907_sum_of_subarray_minimums import Solution


def test_sum_subarray_mins():
    assert Solution.sumSubarrayMins([3, 1, 2, 4]) == 17
    assert Solution.sumSubarrayMins([1, 2, 3, 4]) == 20
