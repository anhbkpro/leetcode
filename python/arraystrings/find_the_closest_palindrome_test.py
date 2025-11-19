from .find_the_closest_palindrome import Solution


def test_nearest_palindromic():
    assert Solution().nearestPalindromic("123") == "121"
    assert Solution().nearestPalindromic("1234") == "1221"
    assert Solution().nearestPalindromic("1000") == "999"
