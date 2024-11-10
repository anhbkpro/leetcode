from .shortest_subarray_with_or_at_least_k_ii import Solution


def test_minimum_subarray_length():
    assert Solution().minimumSubarrayLength(nums=[1, 2, 3], k=2) == 1
    assert Solution().minimumSubarrayLength(nums=[2, 1, 8], k=10) == 3
