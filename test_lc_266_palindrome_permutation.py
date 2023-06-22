from lc_266_palindrome_permutation import can_permute_palindrome


def test_can_permute_palindrome():
    assert can_permute_palindrome(s="code") is False
    assert can_permute_palindrome(s="aab") is True
