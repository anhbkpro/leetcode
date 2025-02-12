from .max_sum_of_a_pair_with_equal_sum_of_digits import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test_calculate_digit_sum(solution):
    # Test single digit numbers
    assert solution._calculate_digit_sum(5) == 5
    assert solution._calculate_digit_sum(9) == 9

    # Test multiple digit numbers
    assert solution._calculate_digit_sum(123) == 6  # 1 + 2 + 3 = 6
    assert solution._calculate_digit_sum(999) == 27  # 9 + 9 + 9 = 27
    assert solution._calculate_digit_sum(10) == 1  # 1 + 0 = 1


def test_maximum_sum_basic(solution):
    # Test case from LeetCode example
    nums = [18, 43, 36, 13, 7]
    assert solution.maximumSum(nums) == 54  # 18 + 36 = 54 (both have digit sum 9)


def test_maximum_sum_no_pairs(solution):
    # Test when no pairs with equal digit sums exist
    nums = [1, 2, 3, 4, 5]
    assert solution.maximumSum(nums) == -1


def test_maximum_sum_multiple_pairs(solution):
    # Test when multiple pairs with equal digit sums exist
    nums = [18, 36, 27, 45]  # 18,36 (sum=9) and 27,45 (sum=9)
    assert solution.maximumSum(nums) == 81  # 36 + 45 = 81


def test_maximum_sum_same_numbers(solution):
    # Test with duplicate numbers
    nums = [18, 18, 18, 18]
    assert solution.maximumSum(nums) == 36  # 18 + 18 = 36


def test_maximum_sum_large_numbers(solution):
    # Test with large numbers
    nums = [999989, 999998, 123456, 123]  # 999989 and 999998 both have digit sum 53
    assert solution.maximumSum(nums) == 1999987  # 999989 + 999998 = 1999987


def test_maximum_sum_single_digit(solution):
    # Test with single digit numbers
    nums = [1, 1, 2, 2, 3, 3]  # pairs with same digits
    assert (
        solution.maximumSum(nums) == 6
    )  # 3 + 3 = 6 (largest pair with same digit sum)


def test_maximum_sum_empty_list(solution):
    # Test with empty list
    nums = []
    assert solution.maximumSum(nums) == -1
