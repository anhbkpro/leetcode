from .final_prices_with_a_special_discount_in_a_shop import Solution


def test_final_prices():
    assert Solution().finalPrices(prices=[8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
