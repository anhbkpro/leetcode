from trie.design_add_and_search_words_data_structure import WordDictionary


# Search for a word that exists in the dictionary
def test_search_existing_word():
    word_dict = WordDictionary()
    word_dict.addWord("example")
    assert word_dict.search("example")


# Search for an empty string
def test_search_empty_string():
    word_dict = WordDictionary()
    assert not word_dict.search("")


# Search for a word that does not exist in the dictionary
def test_search_non_existing_word():
    word_dict = WordDictionary()
    word_dict.addWord("example")
    assert not word_dict.search("examples")


# Search for a word using '.' as a wildcard character
def test_search_wildcard_character():
    word_dict = WordDictionary()
    word_dict.addWord("apple")
    word_dict.addWord("banana")
    word_dict.addWord("cherry")
    assert word_dict.search("a..le")
