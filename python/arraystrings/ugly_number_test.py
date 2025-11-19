from .ugly_number import Solution


def test_is_ugly():
    assert Solution().isUgly(6) == True
    assert Solution().isUgly(8) == True
    assert Solution().isUgly(14) == False
