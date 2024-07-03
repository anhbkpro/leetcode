from .happy_number import Solution


def test_happy_number():
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(2) == False
