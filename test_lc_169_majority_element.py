from lc_169_majority_element import Solution


def test_majority_element():
    assert Solution.majorityElement(nums=[3, 2, 3]) == 3
    assert Solution.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
