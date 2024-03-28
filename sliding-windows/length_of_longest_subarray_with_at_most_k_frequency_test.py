from length_of_longest_subarray_with_at_most_k_frequency import Solution


def test_maxSubarrayLength():
    assert Solution.max_subarray_length([1, 2, 1, 2, 3], 2) == 5
    assert Solution.max_subarray_length(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
