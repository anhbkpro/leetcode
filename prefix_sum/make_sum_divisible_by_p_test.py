from .make_sum_divisible_by_p import Solution


def test_min_subarray():
    assert Solution().minSubarray([3, 1, 4, 2], 6) == 1
    assert Solution().minSubarray([6, 3, 5, 2], 9) == 2
