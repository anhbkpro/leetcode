from .three_consecutive_odds import Solution


def test_three_consecutive_odds():
    assert Solution().threeConsecutiveOdds([2, 6, 4, 1]) == False
    assert Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
