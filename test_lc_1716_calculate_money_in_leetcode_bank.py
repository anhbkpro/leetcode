from lc_1716_calculate_money_in_leetcode_bank import Solution


def test_total_money():
    assert Solution.totalMoney(n=4) == 10
    assert Solution.totalMoney(n=10) == 37
    assert Solution.totalMoney(n=20) == 96
