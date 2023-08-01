from lc_77_combinations import Solution


def test_combine():
    assert Solution.combine(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4],
                                            [3, 4]]
    assert Solution.combine(n=1, k=1) == [[1]]
