from .longest_subarray_with_maximum_bitwise_and import Solution


def test_longest_subarray():
    assert Solution().longestSubarray(nums=[1, 2, 3, 3, 2, 2]) == 2
