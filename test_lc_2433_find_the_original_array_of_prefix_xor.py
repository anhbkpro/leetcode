from lc_2433_find_the_original_array_of_prefix_xor import Solution


def test_find_array():
    assert Solution.findArray(pref=[5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]
    assert Solution.findArray(pref=[13]) == [13]
