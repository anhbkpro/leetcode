from .kth_largest_element_in_an_array import Solution


def test_example_1():
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5
    assert solution.findKthLargest(nums, k) == expected


def test_example_2():
    solution = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    expected = 4
    assert solution.findKthLargest(nums, k) == expected


def test_single_element():
    solution = Solution()
    nums = [1]
    k = 1
    expected = 1
    assert solution.findKthLargest(nums, k) == expected


def test_all_same_elements():
    solution = Solution()
    nums = [2, 2, 2, 2]
    k = 2
    expected = 2
    assert solution.findKthLargest(nums, k) == expected


def test_k_equals_length():
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = len(nums)
    expected = 1
    assert solution.findKthLargest(nums, k) == expected


def test_negative_numbers():
    solution = Solution()
    nums = [-3, -2, -1, -5, -6, -4]
    k = 2
    expected = -2
    assert solution.findKthLargest(nums, k) == expected


def test_mixed_numbers():
    solution = Solution()
    nums = [-1, 2, 0, -3, 4, -2]
    k = 3
    expected = 0
    assert solution.findKthLargest(nums, k) == expected
