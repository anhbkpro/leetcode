from lc_645_set_mismatch import Solution


def test_find_error_nums():
    assert Solution.findErrorNums([1, 2, 2, 4]) == [2, 3]
    assert Solution.findErrorNums([1, 1]) == [1, 2]
