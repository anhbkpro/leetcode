from lc_215_kth_largest_element_in_an_array import Solution


def test_find_kth_largest():
    assert Solution.find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert Solution.find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
