from lc_229_majority_element_ii import Solution


def test_majority_element():
    assert Solution.majorityElement(nums=[3, 2, 3]) == [3]
    assert Solution.majorityElement(nums=[1]) == [1]
    assert Solution.majorityElement(nums=[1, 2]) == [1, 2]
