from mathematics.palindrome_number import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test_single_digit_numbers(solution):
    # Test single digit numbers (all should be palindromes)
    for i in range(10):
        assert solution.isPalindrome(i) == True


def test_two_digit_numbers(solution):
    # Test two digit numbers
    assert solution.isPalindrome(11) == True
    assert solution.isPalindrome(22) == True
    assert solution.isPalindrome(33) == True
    assert solution.isPalindrome(44) == True
    assert solution.isPalindrome(12) == False
    assert solution.isPalindrome(21) == False
    assert solution.isPalindrome(90) == False


def test_three_digit_numbers(solution):
    # Test three digit numbers
    assert solution.isPalindrome(101) == True
    assert solution.isPalindrome(111) == True
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(123) == False
    assert solution.isPalindrome(321) == False
    assert solution.isPalindrome(100) == False


def test_larger_palindromes(solution):
    # Test larger palindrome numbers
    assert solution.isPalindrome(1001) == True
    assert solution.isPalindrome(1111) == True
    assert solution.isPalindrome(1221) == True
    assert solution.isPalindrome(12321) == True
    assert solution.isPalindrome(12344321) == True


def test_larger_non_palindromes(solution):
    # Test larger non-palindrome numbers
    assert solution.isPalindrome(1234) == False
    assert solution.isPalindrome(12345) == False
    assert solution.isPalindrome(10011) == False
    assert solution.isPalindrome(12341) == False


def test_negative_numbers(solution):
    # Test negative numbers (should all be False)
    assert solution.isPalindrome(-1) == False
    assert solution.isPalindrome(-11) == False
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(-12321) == False


def test_zero_ending_numbers(solution):
    # Test numbers ending with 0
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(100) == False
    assert solution.isPalindrome(1000) == False
    assert solution.isPalindrome(10000) == False


def test_edge_cases(solution):
    # Test edge cases
    assert solution.isPalindrome(0) == True  # Zero is a palindrome
    assert solution.isPalindrome(1) == True  # Single digit
    assert solution.isPalindrome(9) == True  # Single digit
    assert solution.isPalindrome(10) == False  # Two digits with zero


def test_repeated_digits(solution):
    # Test numbers with repeated digits
    assert solution.isPalindrome(11) == True
    assert solution.isPalindrome(111) == True
    assert solution.isPalindrome(1111) == True
    assert solution.isPalindrome(11111) == True
    assert solution.isPalindrome(222222) == True


def test_alternating_digits(solution):
    # Test numbers with alternating digits
    assert solution.isPalindrome(101) == True
    assert solution.isPalindrome(12021) == True
    assert solution.isPalindrome(10201) == True
    assert solution.isPalindrome(102210) == False  # Not a palindrome
    assert solution.isPalindrome(10101) == True
