from greedy.maximum_difference_between_increasing_elements import Solution


def test_empty_array():
    solution = Solution()
    assert solution.maximumDifference([]) == -1


def test_single_element():
    solution = Solution()
    assert solution.maximumDifference([1]) == -1
    assert solution.maximumDifference([0]) == -1
    assert solution.maximumDifference([-1]) == -1


def test_two_elements():
    solution = Solution()
    assert solution.maximumDifference([1, 2]) == 1
    assert solution.maximumDifference([2, 1]) == -1
    assert solution.maximumDifference([1, 1]) == -1


def test_three_elements():
    solution = Solution()
    assert solution.maximumDifference([1, 2, 3]) == 2
    assert solution.maximumDifference([3, 2, 1]) == -1
    assert solution.maximumDifference([1, 1, 1]) == -1


def test_negative_numbers():
    solution = Solution()
    assert solution.maximumDifference([-1, -2, -3]) == -1
    assert solution.maximumDifference([-3, -2, -1]) == 2
    assert solution.maximumDifference([-1, -1, -1]) == -1


def test_mixed_numbers():
    solution = Solution()
    assert solution.maximumDifference([1, -2, 3]) == 5
    assert solution.maximumDifference([-2, 1, 3]) == 5
    assert solution.maximumDifference([3, -2, 1]) == 3


def test_leetcode_examples():
    solution = Solution()
    assert solution.maximumDifference([7, 1, 5, 4]) == 4
    assert solution.maximumDifference([9, 4, 3, 2]) == -1
    assert solution.maximumDifference([1, 5, 2, 10]) == 9


def test_repeated_numbers():
    solution = Solution()
    assert solution.maximumDifference([1, 1, 1, 1]) == -1
    assert solution.maximumDifference([1, 2, 2, 2]) == 1
    assert solution.maximumDifference([2, 2, 2, 1]) == -1


def test_ascending_sequence():
    solution = Solution()
    assert solution.maximumDifference([1, 2, 3, 4, 5]) == 4
    assert solution.maximumDifference([0, 1, 2, 3, 4]) == 4
    assert solution.maximumDifference([-2, -1, 0, 1, 2]) == 4


def test_descending_sequence():
    solution = Solution()
    assert solution.maximumDifference([5, 4, 3, 2, 1]) == -1
    assert solution.maximumDifference([4, 3, 2, 1, 0]) == -1
    assert solution.maximumDifference([2, 1, 0, -1, -2]) == -1


def test_large_numbers():
    solution = Solution()
    assert solution.maximumDifference([1000, 2000, 3000]) == 2000
    assert solution.maximumDifference([3000, 2000, 1000]) == -1
    assert solution.maximumDifference([1000, 1000, 1000]) == -1
