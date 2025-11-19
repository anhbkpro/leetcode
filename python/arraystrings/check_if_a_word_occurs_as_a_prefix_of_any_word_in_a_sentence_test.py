from .check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence import Solution


def test_check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence():
    assert Solution().isPrefixOfWord("i love eating burger", "burg") == 4
    assert Solution().isPrefixOfWord("this problem is an easy problem", "pro") == 2
    assert Solution().isPrefixOfWord("i am tired", "you") == -1
