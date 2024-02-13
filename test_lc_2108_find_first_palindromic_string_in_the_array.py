from lc_2108_find_first_palindromic_string_in_the_array import Solution


def test_first_palindrome():
    assert Solution.firstPalindrome(words = ["abc","car","ada","racecar","cool"]) == "ada"
    assert Solution.firstPalindrome(words = ["def","ghi"]) == ""
