from .uncommon_words_from_two_sentences import Solution


def test_uncommon_words_from_two_sentences():
    assert sorted(
        Solution().uncommonFromSentences("this apple is sweet", "this apple is sour")
    ) == sorted(["sweet", "sour"])
