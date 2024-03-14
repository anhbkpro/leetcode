from binary_subarrays_with_sum import Solution


def test_num_subarrays_with_sum():
    assert Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4
    assert Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15
