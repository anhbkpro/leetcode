from .next_greater_element_ii import Solution


def test_next_greater_elements():
    assert Solution().nextGreaterElements(nums=[1, 2, 1]) == [2, -1, 2]
    assert Solution().nextGreaterElements(nums=[1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
