from subarrays_with_k_different_integers import Solution


def test_subarraysWithKDistinct():
    sol = Solution()
    assert sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7
    assert sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3
