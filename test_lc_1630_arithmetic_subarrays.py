from lc_1630_arithmetic_subarrays import Solution


def test_check_arithmetic_subarrays():
    assert Solution.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]) == [True, False, True]
