from lc_135_candy import Solution


def test_candy():
    assert Solution.candy([1, 0, 2]) == 5
    assert Solution.candy([1, 2, 2]) == 4
