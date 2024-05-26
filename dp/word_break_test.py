from dp.word_break import Solution


def test_word_break():
    assert Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]) is True
    assert Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]) is True
    assert Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) is False
