from lc_169_majority_element import Solution


def test_majority_element():
    assert Solution.majority_element(nums = [3, 2, 3]) == 3
    assert Solution.majority_element(nums = [2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_boyer_moore_voting():
    assert Solution.majority_element_boyer_moore_voting(nums = [3,2,3]) == 3
    assert Solution.majority_element_boyer_moore_voting(nums = [2,2,1,1,1,2,2]) == 2
