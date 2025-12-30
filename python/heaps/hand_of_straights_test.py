from heaps.hand_of_straights import Solution


def test_hand_of_straights():
    assert Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert not Solution().isNStraightHand([1, 2, 3, 4, 5], 4)
