import pytest

from arraystrings.three_consecutive_odds import Solution


def test_three_consecutive_odds_typical():
    solution = Solution()
    arr = [2, 6, 4, 1, 3, 5]
    assert solution.threeConsecutiveOdds(arr) is True


def test_three_consecutive_odds_no_consecutive():
    solution = Solution()
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    assert solution.threeConsecutiveOdds(arr) is True


def test_three_consecutive_odds_all_odds():
    solution = Solution()
    arr = [1, 3, 5, 7, 9]
    assert solution.threeConsecutiveOdds(arr) is True


def test_three_consecutive_odds_all_even():
    solution = Solution()
    arr = [2, 4, 6, 8, 10]
    assert solution.threeConsecutiveOdds(arr) is False


def test_three_consecutive_odds_empty():
    solution = Solution()
    arr = []
    assert solution.threeConsecutiveOdds(arr) is False


def test_three_consecutive_odds_short_array():
    solution = Solution()
    arr = [1, 3]
    assert solution.threeConsecutiveOdds(arr) is False


def test_three_consecutive_odds_exactly_three():
    solution = Solution()
    arr = [1, 3, 5]
    assert solution.threeConsecutiveOdds(arr) is True


def test_three_consecutive_odds_reset_count():
    solution = Solution()
    arr = [1, 3, 2, 5, 7, 9]
    assert solution.threeConsecutiveOdds(arr) is True
