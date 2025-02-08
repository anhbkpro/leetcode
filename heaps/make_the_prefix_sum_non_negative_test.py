from .make_the_prefix_sum_non_negative import Solution


def test_example_1():
    solution = Solution()
    nums = [2, -5, 1, -4, 3, -2]
    expected = 2
    assert solution.makePrefSumNonNegative(nums) == expected


def test_example_2():
    solution = Solution()
    nums = [-2, 2, -3, 1]
    expected = 2
    assert solution.makePrefSumNonNegative(nums) == expected


def test_empty_array():
    solution = Solution()
    nums = []
    expected = 0
    assert solution.makePrefSumNonNegative(nums) == expected


def test_all_positive():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    expected = 0
    assert solution.makePrefSumNonNegative(nums) == expected


def test_all_negative():
    solution = Solution()
    nums = [-1, -2, -3, -4, -5]
    expected = 5
    assert solution.makePrefSumNonNegative(nums) == expected


def test_alternating_numbers():
    solution = Solution()
    nums = [1, -1, 1, -1, 1, -1]
    expected = 0
    assert solution.makePrefSumNonNegative(nums) == expected


def test_large_negative_first():
    solution = Solution()
    nums = [-10, 1, 1, 1]
    expected = 1
    assert solution.makePrefSumNonNegative(nums) == expected


def test_multiple_negatives_in_sequence():
    solution = Solution()
    nums = [1, -2, -3, -4, 5]
    expected = 3
    assert solution.makePrefSumNonNegative(nums) == expected


def test_zero_elements():
    solution = Solution()
    nums = [0, 0, 0, 0]
    expected = 0
    assert solution.makePrefSumNonNegative(nums) == expected


def test_single_element_negative():
    solution = Solution()
    nums = [-5]
    expected = 1
    assert solution.makePrefSumNonNegative(nums) == expected


def test_single_element_positive():
    solution = Solution()
    nums = [5]
    expected = 0
    assert solution.makePrefSumNonNegative(nums) == expected


def test_complex_sequence():
    solution = Solution()
    nums = [3, -4, 2, -5, -2, 6, -3]
    expected = 2
    assert solution.makePrefSumNonNegative(nums) == expected
