from lc_734_sentence_similarity import areSentencesSimilar


def test_are_sentences_similar():
    assert areSentencesSimilar(sentence1=["great", "acting", "skills"], sentence2=["fine", "drama", "talent"],
                               similarPairs=[["great", "fine"], ["drama", "acting"], ["skills", "talent"]]) is True
    assert areSentencesSimilar(sentence1=["great"], sentence2=["great"], similarPairs=[]) is True
    assert areSentencesSimilar(sentence1=["great"], sentence2=["doubleplus", "good"],
                               similarPairs=[["great", "doubleplus"]]) is False
