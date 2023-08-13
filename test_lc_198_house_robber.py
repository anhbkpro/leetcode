from lc_198_house_robber import Solution


def test_rob():
    assert Solution.rob(nums=[1, 2, 3, 1]) == 4
    assert Solution.rob(nums=[2, 7, 9, 3, 1]) == 12
