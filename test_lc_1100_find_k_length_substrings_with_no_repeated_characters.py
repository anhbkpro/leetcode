from lc_1100_find_k_length_substrings_with_no_repeated_characters import numKLenSubstrNoRepeats


def test_num_klen_substr_no_repeats():
    assert numKLenSubstrNoRepeats(s="havefunonleetcode", k=5) == 6
    assert numKLenSubstrNoRepeats(s="home", k=5) == 0
