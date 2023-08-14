from lc_740_delete_and_earn import Solution


def test_delete_and_earn():
    assert Solution.deleteAndEarn(nums=[3, 4, 2]) == 6
    assert Solution.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]) == 9
