from .ipo import Solution


def test_findMaximizedCapital():
    assert Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
