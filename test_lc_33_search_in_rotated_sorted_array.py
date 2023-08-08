from lc_33_search_in_rotated_sorted_array import Solution


def test_search():
    assert Solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
