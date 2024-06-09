from .maximum_size_subarray_sum_equals_k import Solution


def test_max_sub_array_len():
    assert Solution.max_sub_array_len([1, -1, 5, -2, 3], 3) == 4
    assert Solution.max_sub_array_len([-2, -1, 2, 1], 1) == 2
