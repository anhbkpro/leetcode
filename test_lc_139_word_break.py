from lc_139_word_break import Solution


def test_word_break():
    assert Solution.wordBreak("leetcode", ["leet", "code"]) is True
    assert Solution.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert Solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
