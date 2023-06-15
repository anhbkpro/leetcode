from lc_1150_check_if_a_number_is_majority_element_in_a_sorted_array_binary_search import is_majority_element_bs


def test_is_majority_element_bs():
    assert is_majority_element_bs(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5) is True
    assert is_majority_element_bs(nums=[10, 100, 101, 101], target=101) is False
