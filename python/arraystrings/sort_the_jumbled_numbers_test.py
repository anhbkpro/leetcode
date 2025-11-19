from .sort_the_jumbled_numbers import Solution


def test_sort_jumbled():
    assert Solution().sortJumbled(
        mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]
    ) == [338, 38, 991]
    assert Solution().sortJumbled(
        mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]
    ) == [123, 456, 789]
