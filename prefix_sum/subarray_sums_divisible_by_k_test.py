from .subarray_sums_divisible_by_k import Solution


def test_subarray_sums_divisible_by_k():
    assert Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7
    assert Solution().subarraysDivByK([5], 9) == 0
