from .minimum_size_subarray_sum import Solution


def test_min_sub_array_len():
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
