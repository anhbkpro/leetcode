from .check_if_an_array_is_consecutive import Solution


def test_is_consecutive():
    assert Solution().isConsecutive([1, 2, 3, 4, 5]) == True
    assert Solution().isConsecutive([1, 2, 3, 5, 6]) == False
