from lc_2482_difference_between_ones_and_zeros_in_row_and_column import Solution


def test_ones_minus_zeros():
    assert Solution.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]) == [[0,0,4],[0,0,4],[-2,-2,2]]
    assert Solution.onesMinusZeros(grid = [[1,1,1],[1,1,1]]) == [[5,5,5],[5,5,5]]
