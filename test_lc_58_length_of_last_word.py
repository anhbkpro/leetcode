from lc_58_length_of_last_word import Solution


def test_length_of_last_word():
    assert Solution.lengthOfLastWord('Hello World') == 5
    assert Solution.lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert Solution.lengthOfLastWord('a ') == 1
