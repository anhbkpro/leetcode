from .find_the_punishment_number_of_an_integer import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test_single_digit(solution):
    # Test n = 1, 1² = 1, can be partitioned as "1" = 1
    assert solution.punishmentNumber(1) == 1


def test_known_punishment_numbers(solution):
    # Test some known punishment numbers
    # 9² = 81, can be partitioned as "8" + "1" = 9
    assert solution.punishmentNumber(9) == 82  # 1 + 81

    # 10² = 100, can be partitioned as "10" + "0" = 10
    assert solution.punishmentNumber(10) == 182  # 82 + 100


def test_non_punishment_numbers(solution):
    # Test numbers that are not punishment numbers
    # 8² = 64, cannot be partitioned to sum to 8
    assert solution.punishmentNumber(8) == 1  # Only includes 1


def test_multiple_valid_partitions(solution):
    # 36² = 1296, can be partitioned as "12" + "9" + "6" = 27
    # or "1" + "2" + "9" + "6" = 18, etc.
    # but none sum to 36, so it's not a punishment number
    result = solution.punishmentNumber(36)
    assert result == 1478  # Includes previous punishment numbers


def test_consecutive_numbers(solution):
    # Test a range of consecutive numbers
    assert solution.punishmentNumber(15) == 182
    assert solution.punishmentNumber(16) == 182
    assert solution.punishmentNumber(17) == 182
    assert solution.punishmentNumber(18) == 182
    assert solution.punishmentNumber(19) == 182


def test_larger_numbers(solution):
    # Test some larger numbers
    assert solution.punishmentNumber(37) == 1478
    assert solution.punishmentNumber(38) == 1478
    assert solution.punishmentNumber(39) == 1478
    assert solution.punishmentNumber(40) == 1478


def test_find_partitions_helper(solution):
    # Test the helper function directly for specific cases
    memo = [[-1] * 10 for _ in range(2)]
    # Test "81" can be partitioned as "8"+"1"=9
    assert solution.find_partitions(0, 0, "81", 9, memo) == True

    memo = [[-1] * 11 for _ in range(3)]
    # Test "100" can be partitioned as "10"+"0"=10
    assert solution.find_partitions(0, 0, "100", 10, memo) == True

    memo = [[-1] * 9 for _ in range(2)]
    # Test "64" cannot be partitioned to sum to 8
    assert solution.find_partitions(0, 0, "64", 8, memo) == False


def test_edge_cases(solution):
    # Test edge cases
    assert solution.punishmentNumber(1) == 1  # Smallest possible input
    assert solution.punishmentNumber(2) == 1  # No valid partition for 2²=4
    assert solution.punishmentNumber(3) == 1  # No valid partition for 3²=9
    assert solution.punishmentNumber(4) == 1  # No valid partition for 4²=16


def test_cumulative_nature(solution):
    # Test that the punishment number is cumulative
    n1 = solution.punishmentNumber(9)  # 1 + 81 = 82
    n2 = solution.punishmentNumber(10)  # 82 + 100 = 182
    assert n2 > n1  # Should be strictly increasing when a punishment number is found
    assert n2 == 182  # Should include all previous punishment numbers
