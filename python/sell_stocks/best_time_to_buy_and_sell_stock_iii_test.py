from sell_stocks.best_time_to_buy_and_sell_stock_iii import Solution


def test_max_profit():
    assert Solution().maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert Solution().maxProfit(prices=[1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0
