from .length_of_longest_subarray_with_at_most_k_frequency import Solution


def test_max_subarray_length():
    assert Solution.max_subarray_length(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2) == 6
    assert Solution.max_subarray_length(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
    assert Solution.max_subarray_length(nums=[5, 5, 5, 5, 5, 5, 5], k=4) == 4
