from lc_487_max_consecutive_ones_ii import findMaxConsecutiveOnes


def test_find_max_consecutive_ones():
    assert findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]) == 4
    assert findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]) == 4
