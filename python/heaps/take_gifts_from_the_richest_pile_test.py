from .take_gifts_from_the_richest_pile import Solution


def test_take_gifts():
    assert Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4) == 29
    assert Solution().pickGifts(gifts=[1, 1, 1, 1], k=4) == 4
