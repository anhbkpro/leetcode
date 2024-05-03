from arraystrings.squares_of_a_sorted_array import Solution


def test_squares_of_a_sorted_array():
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
