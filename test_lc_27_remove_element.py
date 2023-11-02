from lc_27_remove_element import Solution


def test_remove_element():
    assert Solution.removeElement(nums=[3, 2, 2, 3], val=3) == 2
    assert Solution.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5
