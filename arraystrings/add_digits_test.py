from .add_digits import Solution


def test_add_digits():
    assert Solution().addDigits(38) == 2
    assert Solution().addDigits(0) == 0
