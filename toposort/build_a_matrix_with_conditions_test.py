from .build_a_matrix_with_conditions import Solution


def test_restore_matrix():
    assert Solution().buildMatrix(
        k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]]
    ) == [[3, 0, 0], [0, 0, 1], [0, 2, 0]]
