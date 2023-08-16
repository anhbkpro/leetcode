from lc_5_longest_palindromic_substring import Solution


def test_longest_palindrome():
    assert Solution.longest_palindrome(s="babad") in ["bab", "aba"]
    assert Solution.longest_palindrome(s="cbbd") == "bb"
