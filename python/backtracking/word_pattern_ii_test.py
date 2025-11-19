from backtracking.word_pattern_ii import Solution


def test_word_pattern_ii():
    assert Solution().wordPatternMatch("abab", "redblueredblue") is True
    assert Solution().wordPatternMatch("aaaa", "asdasdasdasd") is True
