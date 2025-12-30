from sliding_windows.LC75__max_consecutive_ones_iii import Solution


def test_longest_ones_empty_array():
    solution = Solution()
    assert solution.longestOnes([], 1) == 0
    assert solution.longestOnes([], 0) == 0


def test_longest_ones_all_ones():
    solution = Solution()
    assert solution.longestOnes([1, 1, 1, 1], 0) == 4
    assert solution.longestOnes([1, 1, 1, 1], 1) == 4


def test_longest_ones_all_zeros():
    solution = Solution()
    assert solution.longestOnes([0, 0, 0, 0], 0) == 0
    assert solution.longestOnes([0, 0, 0, 0], 1) == 1
    assert solution.longestOnes([0, 0, 0, 0], 2) == 2


def test_longest_ones_typical_case():
    solution = Solution()
    # Example from LeetCode
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    assert solution.longestOnes(nums, 2) == 6


def test_longest_ones_alternating():
    solution = Solution()
    nums = [1, 0, 1, 0, 1, 0, 1]
    assert solution.longestOnes(nums, 1) == 3
    assert solution.longestOnes(nums, 2) == 5
    assert solution.longestOnes(nums, 3) == 7


def test_longest_ones_consecutive_zeros():
    solution = Solution()
    nums = [1, 1, 0, 0, 0, 1, 1, 1]
    assert solution.longestOnes(nums, 1) == 4
    assert solution.longestOnes(nums, 2) == 5
    assert solution.longestOnes(nums, 3) == 8


def test_longest_ones_k_larger_than_zeros():
    solution = Solution()
    nums = [1, 0, 1, 0, 1]
    assert solution.longestOnes(nums, 3) == 5
    assert solution.longestOnes(nums, 4) == 5


def test_longest_ones_single_element():
    solution = Solution()
    assert solution.longestOnes([1], 0) == 1
    assert solution.longestOnes([0], 0) == 0
    assert solution.longestOnes([0], 1) == 1
    assert solution.longestOnes([1], 1) == 1


def test_longest_ones_complex_case():
    solution = Solution()
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    assert solution.longestOnes(nums, 3) == 10
