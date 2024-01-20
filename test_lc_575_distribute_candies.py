from lc_575_distribute_candies import Solution


def test_distribute_candies():
    assert Solution.distributeCandies([1, 1, 2, 2, 3, 3]) == 3
    assert Solution.distributeCandies([1, 1, 2, 3]) == 2
