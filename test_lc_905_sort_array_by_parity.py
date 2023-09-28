from lc_905_sort_array_by_parity import Solution


def test_sort_array_by_parity():
    assert Solution.sortArrayByParity(A=[3, 1, 2, 4]) == [2, 4, 3, 1]
    assert Solution.sortArrayByParity(A=[1, 0]) == [0, 1]
