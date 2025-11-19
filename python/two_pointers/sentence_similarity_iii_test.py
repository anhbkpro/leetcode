from .sentence_similarity_iii import Solution


def test_are_sentences_similar():
    assert Solution().areSentencesSimilar(s1="My name is Haley", s2="My Haley") is True
    assert Solution().areSentencesSimilar(s1="of", s2="A lot of words") is False
