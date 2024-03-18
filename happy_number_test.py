from happy_number import Solution


def test_isHappy():
    assert Solution().isHappy(19) is True
    assert Solution().isHappy(2) is False
    assert Solution().isHappy(7) is True
