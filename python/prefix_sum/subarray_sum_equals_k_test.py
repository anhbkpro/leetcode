from .subarray_sum_equals_k import Solution


def test_subarray_sum():
    assert Solution.subarray_sum(nums=[1, 1, 1], k=2) == 2
    assert Solution.subarray_sum(nums=[1, 2, 3], k=3) == 2
