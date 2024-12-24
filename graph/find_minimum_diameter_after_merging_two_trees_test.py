from .find_minimum_diameter_after_merging_two_trees import Solution


def test_minimum_diameter_after_merge():
    assert (
        Solution().minimumDiameterAfterMerge(
            edges1=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
            edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        )
        == 5
    )
