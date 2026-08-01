from .predict_the_winner import Solution


def test_predict_the_winner():
    assert Solution().predictTheWinner([1, 5, 2]) is False
    assert Solution().predictTheWinner([1, 5, 233, 7]) is True
    assert Solution().predictTheWinner([1, 1]) is True
    assert Solution().predictTheWinner([5]) is True
    assert Solution().predictTheWinner([2, 4, 55, 6, 8]) is False
