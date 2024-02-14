from lc_1046_last_stone_weight import Solution


def test_last_stone_weight():
    assert Solution.last_stone_weight(stones=[2, 7, 4, 1, 8, 1]) == 1
    assert Solution.last_stone_weight(stones=[2, 2]) == 0
    assert Solution.last_stone_weight(stones=[1]) == 1
