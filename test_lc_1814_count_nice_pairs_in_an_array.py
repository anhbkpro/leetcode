from lc_1814_count_nice_pairs_in_an_array import Solution


def test_count_nice_pairs():
    assert Solution.countNicePairs(nums=[42, 11, 1, 97]) == 2
    assert Solution.countNicePairs(nums=[13, 10, 35, 24, 76]) == 4
