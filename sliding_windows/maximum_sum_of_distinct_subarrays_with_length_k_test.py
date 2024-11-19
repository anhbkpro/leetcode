from .maximum_sum_of_distinct_subarrays_with_length_k import Solution


def test_maximum_subarray_sum():
    assert Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15
    assert Solution().maximumSubarraySum(nums=[4, 4, 4], k=3) == 0
