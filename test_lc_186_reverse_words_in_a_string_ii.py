from lc_186_reverse_words_in_a_string_ii import reverse_words


def test_reverse_words():
    s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    reverse_words(s)
    assert s == ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]
