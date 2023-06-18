from lc_1427_perform_string_shifts import string_shift


def test_string_shift():
    assert string_shift("abc", [[0, 1], [1, 2]]) == "cab"
