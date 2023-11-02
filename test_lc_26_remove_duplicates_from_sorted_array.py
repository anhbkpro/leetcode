from lc_26_remove_duplicates_from_sorted_array import Solution


def test_remove_duplicates():
    assert Solution.removeDuplicates(nums=[1, 1, 2]) == 2
    assert Solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
