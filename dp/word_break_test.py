from dp.word_break import Solution


def test_word_break():
    assert Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]) is True
