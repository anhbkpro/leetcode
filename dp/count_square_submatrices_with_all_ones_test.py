from .count_square_submatrices_with_all_ones import Solution


def test_count_square_submatrices_with_all_ones():
    assert (
        Solution().countSquares(
            matrix=[
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 1, 1, 1],
            ]
        )
        == 15
    )
