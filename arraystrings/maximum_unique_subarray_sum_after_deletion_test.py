from .maximum_unique_subarray_sum_after_deletion import Solution


def test_max_sum_with_positive_numbers():
    """Test cases with positive numbers only"""
    solution = Solution()

    # Test with unique positive numbers
    assert solution.maxSum([1, 2, 3, 4, 5]) == 15  # 1+2+3+4+5 = 15

    # Test with duplicate positive numbers (should sum unique ones)
    assert solution.maxSum([1, 2, 2, 3, 3, 4]) == 10  # 1+2+3+4 = 10

    # Test with single positive number
    assert solution.maxSum([5]) == 5

    # Test with all same positive numbers
    assert solution.maxSum([3, 3, 3, 3]) == 3  # Only unique value


def test_max_sum_with_mixed_numbers():
    """Test cases with both positive and non-positive numbers"""
    solution = Solution()

    # Test with positive and negative numbers
    assert solution.maxSum([1, -2, 3, -4, 5]) == 9  # 1+3+5 = 9

    # Test with positive and zero
    assert solution.maxSum([1, 0, 3, 0, 5]) == 9  # 1+3+5 = 9

    # Test with duplicates in mixed array
    assert solution.maxSum([1, -1, 2, -2, 1, 3]) == 6  # 1+2+3 = 6


def test_max_sum_with_non_positive_numbers():
    """Test cases with only non-positive numbers (zero and negative)"""
    solution = Solution()

    # Test with all negative numbers
    assert solution.maxSum([-1, -2, -3, -4]) == -1  # max(-1, -2, -3, -4) = -1

    # Test with all zeros
    assert solution.maxSum([0, 0, 0]) == 0  # max(0, 0, 0) = 0

    # Test with negative numbers and zeros
    assert solution.maxSum([-5, 0, -3, -1]) == 0  # max(-5, 0, -3, -1) = 0

    # Test with single negative number
    assert solution.maxSum([-10]) == -10


def test_max_sum_with_empty_array():
    """Test case with empty array"""
    solution = Solution()

    # This should raise an error since max() on empty list fails
    try:
        solution.maxSum([])
        assert False, "Expected ValueError for empty array"
    except ValueError:
        pass


def test_max_sum_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    # Test with large numbers
    assert solution.maxSum([1000000, 2000000, 3000000]) == 6000000

    # Test with very small positive numbers
    assert solution.maxSum([0.1, 0.2, 0.3]) == 0.6

    # Test with one positive and many negatives
    assert solution.maxSum([5, -1, -2, -3, -4]) == 5

    # Test with many positives and one negative
    assert solution.maxSum([1, 2, 3, 4, -5]) == 10  # 1+2+3+4 = 10


def test_max_sum_with_duplicates():
    """Test cases focusing on duplicate handling"""
    solution = Solution()

    # Test with all duplicates
    assert solution.maxSum([2, 2, 2, 2, 2]) == 2

    # Test with some duplicates
    assert solution.maxSum([1, 1, 2, 2, 3, 3, 4]) == 10  # 1+2+3+4 = 10

    # Test with duplicates in negative numbers
    assert solution.maxSum([-1, -1, -2, -2, -3]) == -1  # max(-1, -1, -2, -2, -3) = -1
