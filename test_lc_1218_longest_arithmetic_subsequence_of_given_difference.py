from lc_1218_longest_arithmetic_subsequence_of_given_difference import longest_subsequence


def test_longest_subsequence():
    assert longest_subsequence([1, 2, 3, 4], 1) == 4
    assert longest_subsequence([1, 3, 5, 7], 1) == 1
    assert longest_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
