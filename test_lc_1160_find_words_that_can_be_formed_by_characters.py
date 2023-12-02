from lc_1160_find_words_that_can_be_formed_by_characters import Solution


def test_count_characters():
    assert Solution.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
    assert Solution.countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10
