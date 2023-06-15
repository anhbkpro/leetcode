from lc_163_missing_ranges import find_missing_ranges


def test_find_missing_ranges():
    assert find_missing_ranges(nums=[0, 1, 3, 50, 75], lower=0, upper=99) == [[2, 2], [4, 49], [51, 74], [76, 99]]
