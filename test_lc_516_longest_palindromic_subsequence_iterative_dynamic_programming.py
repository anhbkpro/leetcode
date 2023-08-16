from lc_516_longest_palindromic_subsequence_iterative_dynamic_programming import Solution


def test_longest_palindrome_subseq():
    assert Solution.longest_palindrome_subseq(s="bbbab") == 4
    assert Solution.longest_palindrome_subseq(s="cbbd") == 2
