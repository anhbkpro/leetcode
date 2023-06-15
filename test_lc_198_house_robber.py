from lc_198_house_robber import rob


def test_rob():
    assert rob(nums=[1, 2, 3, 1]) == 4
    assert rob(nums=[2, 7, 9, 3, 1]) == 12
