from binary_subarrays_with_sum import Solution


def test_num_sub_arrays_with_sum():
    assert Solution.num_sub_arrays_with_sum([1, 0, 1, 0, 1], 2) == 4
    assert Solution.num_sub_arrays_with_sum([0, 0, 0, 0, 0], 0) == 15
