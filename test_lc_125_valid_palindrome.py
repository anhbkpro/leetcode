from lc_125_valid_palindrome import Solution


def test_is_palindrome():
    assert Solution.isPalindrome(s="A man, a plan, a canal: Panama") is True
    assert Solution.isPalindrome(s="race a car") is False
    assert Solution.isPalindrome(s="0P") is False
    assert Solution.isPalindrome(s=" ") is True
