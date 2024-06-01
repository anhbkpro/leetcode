from strings.length_of_last_word import Solution


def test_length_of_last_word():
    assert Solution.length_of_last_word("Hello World") == 5
    assert Solution.length_of_last_word("Hello") == 5
    assert Solution.length_of_last_word("Hello ") == 5
