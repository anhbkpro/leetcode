from trie.design_add_and_search_words_data_structure import WordDictionary


# Search for a word that exists in the dictionary
def test_search_existing_word():
    word_dict = WordDictionary()
    word_dict.addWord("example")
    assert word_dict.search("example") == True

# Search for an empty string
def test_search_empty_string():
    word_dict = WordDictionary()
    assert word_dict.search("") == False

# Search for a word that does not exist in the dictionary
def test_search_non_existing_word():
    word_dict = WordDictionary()
    word_dict.addWord("example")
    assert word_dict.search("examples") == False

# Search for a word that has a dot in it
def test_search_word_with_dot():
    word_dict = WordDictionary()
    word_dict.addWord("example")
    assert word_dict.search("exa.ple") == True
