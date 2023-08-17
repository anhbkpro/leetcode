from lc_72_edit_distance import Solution


def test_my_min_distance():
    assert Solution.min_distance(word1="horse", word2="ros") == 3
    assert Solution.min_distance(word1="intention", word2="execution") == 5
    assert Solution.min_distance(word1="a", word2="ab") == 1
