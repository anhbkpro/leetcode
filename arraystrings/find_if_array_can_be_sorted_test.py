from .find_if_array_can_be_sorted import Solution


def test_find_if_array_can_be_sorted():
    assert Solution().canBeSorted(nums=[1, 2, 3, 4, 5]) == True
    assert Solution().canBeSorted(nums=[8, 4, 2, 30, 15]) == True
