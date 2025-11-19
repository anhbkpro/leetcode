from .relative_sort_array import Solution


def test_relative_sort_array():
    assert Solution().relativeSortArray(
        arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
    ) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
