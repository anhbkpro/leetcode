from lc_1198_find_smallest_common_element_in_all_rows import smallestCommonElement


def test_smallest_common_element():
    assert smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]) == 5
    assert smallestCommonElement([[1, 2, 3], [2, 3, 4], [2, 3, 5]]) == 2
