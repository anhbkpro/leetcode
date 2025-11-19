from .longest_palindrome import Solution


def test_longest_palindrome():
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("a") == 1
