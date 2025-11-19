from .find_missing_observations import Solution


def test_find_missing_observations():
    assert Solution().missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2) == [6, 6]
    assert Solution().missingRolls(rolls=[1, 5, 6], mean=3, n=4) == [3, 2, 2, 2]
    assert Solution().missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4) == []
