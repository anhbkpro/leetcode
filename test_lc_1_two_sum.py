from lc_1_two_sum import twoSum, twoSum2Loops


def test_two_sum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum2loops():
    assert twoSum2Loops([2, 7, 11, 15], 9) == [0, 1]
