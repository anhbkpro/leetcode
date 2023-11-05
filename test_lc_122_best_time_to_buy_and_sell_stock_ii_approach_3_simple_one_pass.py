from lc_122_best_time_to_buy_and_sell_stock_ii_approach_3_simple_one_pass import Solution


def test_max_profit():
    assert Solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution.maxProfit([7, 6, 4, 3, 1]) == 0
