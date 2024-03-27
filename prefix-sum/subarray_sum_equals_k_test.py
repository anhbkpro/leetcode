from lc_560_subarray_sum_equals_k import Solution


def test_subarray_sum():
    assert Solution.subarraySum(nums=[1, 1, 1], k=2) == 2
    assert Solution.subarraySum(nums=[1, 2, 3], k=3) == 2
