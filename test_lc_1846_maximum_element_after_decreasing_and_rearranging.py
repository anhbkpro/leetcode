from lc_1846_maximum_element_after_decreasing_and_rearranging import Solution


def test_maximum_element_after_decrementing_and_rearranging():
    assert Solution.maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1]) == 2
    assert Solution.maximumElementAfterDecrementingAndRearranging(arr=[100, 1, 1000]) == 3
