from lc_1458_max_dot_product_of_two_subsequences import Solution


def test_max_dot_product():
    assert Solution.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]) == 18
    assert Solution.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]) == 21
    assert Solution.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]) == -1
