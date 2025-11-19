from arraystrings.maximum_difference_between_adjacent_elements_in_a_circular_array import (
    Solution,
)


def test_empty_list():
    solution = Solution()
    assert solution.maxAdjacentDistance([]) == 0


def test_single_element():
    solution = Solution()
    assert solution.maxAdjacentDistance([1]) == 0


def test_two_elements():
    solution = Solution()
    assert solution.maxAdjacentDistance([1, 2]) == 1
    assert solution.maxAdjacentDistance([2, 1]) == 1
    assert solution.maxAdjacentDistance([-1, 1]) == 2


def test_three_elements():
    solution = Solution()
    assert solution.maxAdjacentDistance([1, 2, 3]) == 2
    assert solution.maxAdjacentDistance([3, 1, 2]) == 2
    assert solution.maxAdjacentDistance([2, 3, 1]) == 2


def test_negative_numbers():
    solution = Solution()
    assert solution.maxAdjacentDistance([-1, -2, -3]) == 2
    assert solution.maxAdjacentDistance([-3, -1, -2]) == 2
    assert solution.maxAdjacentDistance([-2, -3, -1]) == 2


def test_mixed_numbers():
    solution = Solution()
    assert solution.maxAdjacentDistance([1, -2, 3, -4]) == 7
    assert solution.maxAdjacentDistance([-4, 1, -2, 3]) == 7
    assert solution.maxAdjacentDistance([3, -4, 1, -2]) == 7


def test_large_numbers():
    solution = Solution()
    assert solution.maxAdjacentDistance([1000, -1000, 2000, -2000]) == 4000
    assert solution.maxAdjacentDistance([-2000, 1000, -1000, 2000]) == 4000
    assert solution.maxAdjacentDistance([2000, -2000, 1000, -1000]) == 4000
