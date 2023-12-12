from lc_1464_maximum_product_of_two_elements_in_an_array import Solution


def test_max_product():
    assert Solution.maxProduct(nums=[3, 4, 5, 2]) == 12
    assert Solution.maxProduct(nums=[1, 5, 4, 5]) == 16
