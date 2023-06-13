from lc_2352_equal_row_and_column_pairs_trie import equalPairs


def test_equal_pairs():
    assert equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
    assert equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
