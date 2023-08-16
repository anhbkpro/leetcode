from lc_516_longest_palindromic_subsequence_dynamic_programming_with_space_optimization import Solution


def test_longest_palindrome_subseq():
    assert Solution.longest_palindrome_subseq(s="bbbab") == 4
    assert Solution.longest_palindrome_subseq(s="cbbd") == 2
