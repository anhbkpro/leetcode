from hashing.continuous_subarray_sum import Solution


def test_continuous_subarray_sum():
    assert Solution().checkSubarraySum([23, 2, 4, 6, 7], 6) == True
    assert Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) == True
    assert Solution().checkSubarraySum([23, 2, 6, 4, 7], 13) == False
