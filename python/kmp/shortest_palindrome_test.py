from .shortest_palindrome import Solution


def test_shortest_palindrome():
    assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert Solution().shortestPalindrome("abcd") == "dcbabcd"
