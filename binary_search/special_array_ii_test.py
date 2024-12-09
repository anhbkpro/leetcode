from .special_array_ii import Solution


def test_is_array_special():
    assert Solution().isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]) == [False]
    assert Solution().isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]) == [
        False,
        True,
    ]
