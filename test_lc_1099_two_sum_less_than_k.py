from lc_1099_two_sum_less_than_k import twoSumLessThanK


def test_1099_two_sum_less_than_k():
    assert twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60) == 58
    assert twoSumLessThanK([10, 20, 30], 15) == -1
