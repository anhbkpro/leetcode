from .maximum_subarray import Solution


def test_maxSubArray():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([1]) == 1
