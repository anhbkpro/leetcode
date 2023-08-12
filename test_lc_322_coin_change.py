from lc_322_coin_change import Solution


def test_coin_change():
    assert Solution.coinChange([1, 2, 5], 11) == 3
    assert Solution.coinChange([2], 3) == -1
    assert Solution.coinChange([1], 0) == 0
