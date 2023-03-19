from lc_211_design_add_and_search_words_data_structure import WordDictionary


def test_word_dictionary():
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    assert obj.search('pad') == False
    assert obj.search('bad') == True
    assert obj.search('.ad') == True
    assert obj.search('b..') == True
