from lc_81_search_in_rotated_sorted_array_ii import Solution


def test_search():
    assert Solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0) is True
    assert Solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) is False
