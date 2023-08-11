from lc_518_coin_change_ii_dp_bottom_up import Solution


def test_change():
    assert Solution.change(amount=5, coins=[1, 2, 5]) == 4
    assert Solution.change(amount=3, coins=[2]) == 0
    assert Solution.change(amount=10, coins=[10]) == 1
