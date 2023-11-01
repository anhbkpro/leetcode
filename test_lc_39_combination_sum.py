from lc_39_combination_sum import Solution


def test_combination_sum():
    assert Solution.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    assert Solution.combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
