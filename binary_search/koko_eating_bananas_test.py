from .koko_eating_bananas import Solution


def test_koko_eating_bananas():
    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
