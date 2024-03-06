from lc_1004_max_consecutive_ones_iii import Solution


def test_longest_ones():
    assert Solution.longest_ones(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
    assert Solution.longest_ones(nums=[0, 0, 0, 1], k=4) == 4
    assert (
        Solution.longest_ones(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
        )
        == 10
    )
