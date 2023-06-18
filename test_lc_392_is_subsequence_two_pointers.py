from lc_392_is_subsequence_two_pointers import is_subsequence


def test_is_subsequence():
    assert is_subsequence("abc", "ahbgdc") is True
    assert is_subsequence("axc", "ahbgdc") is False
