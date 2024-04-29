from sell_stocks.best_time_to_buy_and_sell_stock import Solution


def test_max_profit():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
