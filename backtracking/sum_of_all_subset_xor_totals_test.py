from backtracking.sum_of_all_subset_xor_totals import Solution


def test_sum_of_all_subset_xor_totals():
    assert Solution().subsetXORSum([1, 3]) == 6
    assert Solution().subsetXORSum([5, 1, 6]) == 28
