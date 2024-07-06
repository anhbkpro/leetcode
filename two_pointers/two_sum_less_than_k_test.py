from .two_sum_less_than_k import Solution


def test_two_sum_less_than_k():
    assert Solution().twoSumLessThanK(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60) == 58
    assert Solution().twoSumLessThanK(nums=[10, 20, 30], k=15) == -1
