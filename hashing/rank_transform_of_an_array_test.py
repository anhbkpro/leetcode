from .rank_transform_of_an_array import Solution


def test_array_rank_transform():
    assert Solution().arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
    assert Solution().arrayRankTransform([100, 100, 100]) == [1, 1, 1]
