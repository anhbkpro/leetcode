from lc_414_third_maximum_number import Solution


def test_third_max():
    assert Solution().thirdMax(nums=[3, 2, 1]) == 1
    assert Solution().thirdMax(nums=[1, 2]) == 2
