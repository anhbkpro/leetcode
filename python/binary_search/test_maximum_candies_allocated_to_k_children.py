import pytest

from .maximum_candies_allocated_to_k_children import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    test_cases = [
        (
            [5, 8, 6],
            4,  # k children
            4,  # Each child can get 4 candies (8//4 + 6//4 + 5//4 = 4 children)
        ),
        (
            [2, 5],
            11,  # k children
            0,  # Cannot allocate evenly
        ),
        (
            [1, 2, 3, 4, 10],
            5,  # k children
            3,  # Each child can get 3 candies (10//3 + 4//3 + 3//3 = 5 children)
        ),
    ]
    for candies, k, expected in test_cases:
        assert solution.maximumCandies(candies, k) == expected


def test_edge_cases(solution):
    test_cases = [
        (
            [1],
            1,  # Single child
            1,  # All candies to one child
        ),
        (
            [100],
            5,  # Multiple children, single pile
            20,  # Each child gets 20 candies
        ),
        (
            [1, 1, 1],
            5,  # More children than candies
            0,  # Cannot allocate evenly
        ),
        (
            [0],
            1,  # Zero candies
            0,  # Cannot allocate any
        ),
    ]
    for candies, k, expected in test_cases:
        assert solution.maximumCandies(candies, k) == expected


def test_special_cases(solution):
    test_cases = [
        (
            [10, 10, 10, 10],
            4,  # k equals number of piles
            10,  # Each child gets one full pile
        ),
        (
            [7, 7, 7, 7],
            8,  # Need to split piles
            3,  # Each child gets 3 candies
        ),
        (
            [6, 6, 6, 6],
            12,  # Need to split each pile into 3
            2,  # Each child gets 2 candies
        ),
    ]
    for candies, k, expected in test_cases:
        assert solution.maximumCandies(candies, k) == expected


def test_binary_search_specific(solution):
    """Test cases specifically designed for binary search edge cases"""
    test_cases = [
        (
            [1000000] * 5,  # Large equal piles
            10,  # k children
            500000,  # Each child gets half of a pile
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Increasing sequence
            5,  # k children
            6,  # Each child can get 6 candies (10//6 + 9//6 + 8//6 + 7//6 + 6//6 = 5 children)
        ),
        (
            [2, 4, 6, 8, 10],  # Even numbers sequence
            4,  # k children
            5,  # Each child can get 5 candies (10//5 + 8//5 + 6//5 = 4 children)
        ),
    ]
    for candies, k, expected in test_cases:
        assert solution.maximumCandies(candies, k) == expected


def test_can_allocate_helper(solution):
    """Test the helper function directly"""
    test_cases = [
        (
            [7, 7, 7],  # candies
            3,  # k children
            7,  # target candies per child
            True,  # Can allocate 7 candies to each child
        ),
        (
            [5, 5, 5],
            4,  # More children than piles
            5,  # target candies per child
            False,  # Cannot allocate 5 to each
        ),
        (
            [10, 20, 30],
            6,  # Multiple children
            10,  # target candies per child
            True,  # Can allocate 10 to each
        ),
        (
            [3, 3, 3],
            3,  # Equal to number of piles
            4,  # More than available per pile
            False,  # Cannot allocate 4 to each
        ),
    ]
    for candies, k, target, expected in test_cases:
        assert solution._can_allocate_candies(candies, k, target) == expected
