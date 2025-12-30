import pytest

from mathematics.palindrome_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_digit_numbers(solution):
    # Test single digit numbers (all should be palindromes)
    for i in range(10):
        assert solution.isPalindrome(i)


def test_two_digit_numbers(solution):
    # Test two digit numbers
    assert solution.isPalindrome(11)
    assert solution.isPalindrome(22)
    assert solution.isPalindrome(33)
    assert solution.isPalindrome(44)
    assert not solution.isPalindrome(12)
    assert not solution.isPalindrome(21)
    assert not solution.isPalindrome(90)


def test_three_digit_numbers(solution):
    # Test three digit numbers
    assert solution.isPalindrome(101)
    assert solution.isPalindrome(111)
    assert solution.isPalindrome(121)
    assert not solution.isPalindrome(123)
    assert not solution.isPalindrome(321)
    assert not solution.isPalindrome(100)


def test_larger_palindromes(solution):
    # Test larger palindrome numbers
    assert solution.isPalindrome(1001)
    assert solution.isPalindrome(1111)
    assert solution.isPalindrome(1221)
    assert solution.isPalindrome(12321)
    assert solution.isPalindrome(12344321)


def test_larger_non_palindromes(solution):
    # Test larger non-palindrome numbers
    assert not solution.isPalindrome(1234)
    assert not solution.isPalindrome(12345)
    assert not solution.isPalindrome(10011)
    assert not solution.isPalindrome(12341)


def test_negative_numbers(solution):
    # Test negative numbers (should all be False)
    assert not solution.isPalindrome(-1)
    assert not solution.isPalindrome(-11)
    assert not solution.isPalindrome(-121)
    assert not solution.isPalindrome(-12321)


def test_zero_ending_numbers(solution):
    # Test numbers ending with 0
    assert not solution.isPalindrome(10)
    assert not solution.isPalindrome(100)
    assert not solution.isPalindrome(1000)
    assert not solution.isPalindrome(10000)


def test_edge_cases(solution):
    # Test edge cases
    assert solution.isPalindrome(0)  # Zero is a palindrome
    assert solution.isPalindrome(1)  # Single digit
    assert solution.isPalindrome(9)  # Single digit
    assert not solution.isPalindrome(10)  # Two digits with zero


def test_repeated_digits(solution):
    # Test numbers with repeated digits
    assert solution.isPalindrome(11)
    assert solution.isPalindrome(111)
    assert solution.isPalindrome(1111)
    assert solution.isPalindrome(11111)
    assert solution.isPalindrome(222222)


def test_alternating_digits(solution):
    # Test numbers with alternating digits
    assert solution.isPalindrome(101)
    assert solution.isPalindrome(12021)
    assert solution.isPalindrome(10201)
    assert not solution.isPalindrome(102210)  # Not a palindrome
    assert solution.isPalindrome(10101)
