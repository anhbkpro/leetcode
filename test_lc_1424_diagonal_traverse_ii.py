from lc_1424_diagonal_traverse_ii import Solution


def test_find_diagonal_order():
    assert Solution.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 2, 7, 5, 3, 8, 6, 9]
