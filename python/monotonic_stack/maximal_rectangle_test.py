from .maximal_rectangle import Solution


def test_maximal_rectangle():
    assert (
        Solution().maximalRectangle(
            matrix=[
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
        == 6
    )
    assert Solution().maximalRectangle(matrix=[]) == 0
    assert Solution().maximalRectangle(matrix=[["0"]]) == 0
