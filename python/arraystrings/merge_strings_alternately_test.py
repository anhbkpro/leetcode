from .merge_strings_alternately import Solution


def test_equal_length():
    assert Solution().mergeAlternately("abc", "pqr") == "apbqcr"


def test_word1_longer():
    assert Solution().mergeAlternately("abcd", "pq") == "apbqcd"


def test_word2_longer():
    assert Solution().mergeAlternately("ab", "pqrs") == "apbqrs"


def test_empty_word1():
    assert Solution().mergeAlternately("", "abc") == "abc"


def test_empty_word2():
    assert Solution().mergeAlternately("abc", "") == "abc"
