from .the_earliest_moment_when_everyone_become_friends import Solution


def test_earliest_moment():
    assert (
        Solution().earliestAcq(
            logs=[[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]],
            n=6,
        )
        == 20190301
    )
