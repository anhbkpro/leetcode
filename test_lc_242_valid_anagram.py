from lc_242_valid_anagram import Solution


def test_is_anagram():
    assert Solution.isAnagram(s="anagram", t="nagaram") is True
    assert Solution.isAnagram(s="rat", t="car") is False
