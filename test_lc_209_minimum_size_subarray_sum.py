from lc_209_minimum_size_subarray_sum import minSubArrayLen


def test_min_sub_array_len():
    assert minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert minSubArrayLen(4, [1, 4, 4]) == 1
