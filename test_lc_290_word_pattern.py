from lc_290_word_pattern import Solution


def test_word_pattern():
    assert Solution.wordPattern(pattern='abba', s='dog cat cat dog') is True
    assert Solution.wordPattern(pattern='abba', s='dog cat cat fish') is False
    assert Solution.wordPattern(pattern='aaaa', s='dog cat cat dog') is False
