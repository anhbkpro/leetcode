from lc_486_predict_the_winner import Solution


def test_predict_the_winner():
    assert Solution.predict_the_winner(nums=[1, 5, 2]) is False
    assert Solution.predict_the_winner(nums=[1, 5, 233, 7]) is True
