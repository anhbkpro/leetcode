from lc_137_single_number_ii import singleNumber


def test_single_number():
    assert singleNumber([2, 2, 3, 2]) == 3
    assert singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
