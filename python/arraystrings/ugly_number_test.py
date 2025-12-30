from .ugly_number import Solution


def test_is_ugly():
    assert Solution().isUgly(6)
    assert Solution().isUgly(8)
    assert not Solution().isUgly(14)
