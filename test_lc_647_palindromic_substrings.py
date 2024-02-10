from lc_647_palindromic_substrings import Solution


def test_count_substrings():
    assert Solution.count_substrings_dp(s = "abc") == 3
    assert Solution.count_substrings_dp(s = "aaa") == 6
