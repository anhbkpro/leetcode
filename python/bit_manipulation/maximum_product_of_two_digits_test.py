from .maximum_product_of_two_digits import Solution


def test_max_product():
    assert Solution().maxProduct(31) == 3
    assert Solution().maxProduct(22) == 4
    assert Solution().maxProduct(124) == 8
    assert Solution().maxProduct(999) == 81
    assert Solution().maxProduct(9) == 0
