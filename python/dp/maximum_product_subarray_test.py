from .maximum_product_subarray import Solution


def test_max_product():
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-2, 0, -1]) == 0
