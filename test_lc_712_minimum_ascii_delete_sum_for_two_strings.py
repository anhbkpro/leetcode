from lc_712_minimum_ascii_delete_sum_for_two_strings import Solution


def test_minimum_delete_sum():
    assert Solution.minimumDeleteSum(s1="sea", s2="eat") == 231
    assert Solution.minimumDeleteSum(s1="delete", s2="leet") == 403
    assert Solution.minimumDeleteSum(s1="ccaccjp", s2="fwosarcwge") == 1399
