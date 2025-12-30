from .happy_number import Solution


def test_happy_number():
    assert Solution().isHappy(19)
    assert not Solution().isHappy(2)
