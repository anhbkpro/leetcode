from lc_1060_missing_element_in_sorted_array import missing_element_approach1_iteration


def test_missing_element_approach1_iteration():
    assert missing_element_approach1_iteration(nums=[4, 7, 9, 10], k=1) == 5
    assert missing_element_approach1_iteration(nums=[4, 7, 9, 10], k=3) == 8
    assert missing_element_approach1_iteration(nums=[1, 2, 4], k=3) == 6
