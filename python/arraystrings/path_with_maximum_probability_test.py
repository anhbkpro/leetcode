from .path_with_maximum_probability import Solution


def test_max_probability():
    assert (
        Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
        == 0.25
    )
