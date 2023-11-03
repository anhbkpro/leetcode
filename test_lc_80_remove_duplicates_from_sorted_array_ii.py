from lc_80_remove_duplicates_from_sorted_array_ii import Solution


def test_remove_duplicates():
    assert Solution.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]) == 5
    assert Solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
