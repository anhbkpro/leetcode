from lc_268_missing_number import Solution


def test_missing_number():
    assert Solution.missing_number([3, 0, 1]) == 2
    assert Solution.missing_number([0, 1]) == 2
    assert Solution.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
