from lc_859_buddy_strings import buddyStrings


def test_buddy_strings():
    assert buddyStrings("ab", "ba") is True
    assert buddyStrings("ab", "ab") is False
    assert buddyStrings("aa", "aa") is True
    assert buddyStrings("aaaaaaabc", "aaaaaaacb") is True
