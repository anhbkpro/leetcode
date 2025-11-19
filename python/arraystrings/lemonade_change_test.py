from .lemonade_change import Solution


def test_lemonade_change():
    assert Solution().lemonadeChange(bills=[5, 5, 5, 10, 20]) is True
    assert Solution().lemonadeChange(bills=[5, 5, 10, 10, 20]) is False
