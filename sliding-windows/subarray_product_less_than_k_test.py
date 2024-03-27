from subarray_product_less_than_k import Solution


def test_numSubarrayProductLessThanK():
    assert Solution.num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
    assert Solution.num_subarray_product_less_than_k([1, 2, 3], 0) == 0
    assert Solution.num_subarray_product_less_than_k([1, 1, 1], 1) == 0
