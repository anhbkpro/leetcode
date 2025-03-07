import pytest
from .closest_prime_numbers_in_range import Solution


@pytest.fixture
def solution():
    return Solution()


def test_sieve_small_upper_limit(solution):
    upper_limit = 10
    expected = [False, False, True, True, False, True, False, True, False, False, False]
    assert solution._sieve(upper_limit) == expected


def test_sieve_large_upper_limit(solution):
    upper_limit = 20
    expected = [
        False,
        False,
        True,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
    ]
    assert solution._sieve(upper_limit) == expected


def test_sieve_upper_limit_zero_and_one(solution):
    upper_limit = 1
    expected = [False, False]
    assert solution._sieve(upper_limit) == expected


def test_sieve_upper_limit_prime_number(solution):
    upper_limit = 13
    expected = [
        False,
        False,
        True,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
    ]
    assert solution._sieve(upper_limit) == expected


def test_sieve_upper_limit_non_prime_number(solution):
    upper_limit = 15
    expected = [
        False,
        False,
        True,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
    ]
    assert solution._sieve(upper_limit) == expected


def test_closest_primes_no_primes(solution):
    left = 14
    right = 16
    expected = (-1, -1)
    assert solution.closestPrimes(left, right) == expected


def test_closest_primes_single_prime(solution):
    left = 10
    right = 11
    expected = (-1, -1)
    assert solution.closestPrimes(left, right) == expected


def test_closest_primes_multiple_primes(solution):
    left = 10
    right = 20
    expected = (11, 13)
    assert solution.closestPrimes(left, right) == expected


def test_closest_primes_large_range(solution):
    left = 1
    right = 100
    expected = (2, 3)
    assert solution.closestPrimes(left, right) == expected


def test_closest_primes_adjacent_primes(solution):
    left = 29
    right = 31
    expected = (29, 31)
    assert solution.closestPrimes(left, right) == expected
