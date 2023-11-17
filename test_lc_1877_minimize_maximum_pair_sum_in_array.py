from lc_1877_minimize_maximum_pair_sum_in_array import Solution


def test_min_pair_sum():
    assert Solution.minPairSum(nums=[3, 5, 2, 3]) == 7
    assert Solution.minPairSum(nums=[3, 5, 4, 2, 4, 6]) == 8
