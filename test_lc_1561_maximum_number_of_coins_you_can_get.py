from lc_1561_maximum_number_of_coins_you_can_get import Solution


def test_max_coins():
    assert Solution.maxCoins(piles=[2, 4, 1, 2, 7, 8]) == 9
    assert Solution.maxCoins(piles=[2, 4, 5]) == 4
    assert Solution.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
