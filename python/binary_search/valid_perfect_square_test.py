from .valid_perfect_square import Solution


def test_valid_perfect_square():
    assert Solution().isPerfectSquare(16)
    assert not Solution().isPerfectSquare(14)
