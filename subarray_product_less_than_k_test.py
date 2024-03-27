from subarray_product_less_than_k import Solution


def test_numSubarrayProductLessThanK():
    sol = Solution()
    assert sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert sol.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
    assert sol.numSubarrayProductLessThanK([1, 1, 1], 1) == 0
