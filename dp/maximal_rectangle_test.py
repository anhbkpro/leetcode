from dp.maximal_rectangle import Solution


def test_maximalRectangle():
    assert (
        Solution().maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
        == 6
    )
    assert Solution().maximalRectangle([["0", "1"], ["1", "0"]]) == 1
