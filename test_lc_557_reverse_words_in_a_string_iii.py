from lc_557_reverse_words_in_a_string_iii import Solution


def test_reverse_words():
    assert Solution.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert Solution.reverseWords(s="God Ding") == "doG gniD"


def test_reverse_words2pointers():
    assert Solution.reverseWords2Pointers(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert Solution.reverseWords2Pointers(s="God Ding") == "doG gniD"
