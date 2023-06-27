from lc_373_find_k_pairs_with_smallest_sums import kSmallestPairs


def test_k_smallest_pairs():
    assert kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
