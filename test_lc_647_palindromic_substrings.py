from lc_647_palindromic_substrings import Solution


def test_count_substrings():
    assert Solution.countSubstrings(s="abc") == 3
    assert Solution.countSubstrings(s="aaa") == 6
