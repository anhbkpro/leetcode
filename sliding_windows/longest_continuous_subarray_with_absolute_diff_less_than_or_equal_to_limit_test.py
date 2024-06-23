from .longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit import Solution


def test_longestSubarray():
    assert Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4) == 2
    assert Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5) == 4
