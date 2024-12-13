from .cutting_ribbons import Solution


def test_max_length():
    assert Solution().maxLength(ribbons=[9, 7, 5], k=3) == 5
    assert Solution().maxLength(ribbons=[7, 5, 9], k=4) == 4
