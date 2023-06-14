from lc_72_edit_distance import min_distance


def test_my_min_distance():
    assert min_distance(word1="horse", word2="ros") == 3
    assert min_distance(word1="intention", word2="execution") == 5
