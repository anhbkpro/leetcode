from .circular_sentence import Solution


def test_circular_sentence():
    assert Solution().isCircularSentence("leetcode exercises sound delightful")
    assert not Solution().isCircularSentence("hello world")
