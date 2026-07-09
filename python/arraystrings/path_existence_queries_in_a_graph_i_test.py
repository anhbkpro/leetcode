import pytest
from .path_existence_queries_in_a_graph_i import Solution


@pytest.fixture
def sol():
    return Solution()


def test_single_element(sol):
    n = 1
    nums = [5]
    max_diff = 3
    queries = [[0, 0]]

    assert sol.pathExistenceQueries(n, nums, max_diff, queries) == [True]


def test_all_connected(sol):
    n = 5
    nums = [1, 2, 3, 4, 5]
    max_diff = 1
    queries = [
        [0, 4],
        [1, 3],
        [2, 2],
    ]

    assert sol.pathExistenceQueries(n, nums, max_diff, queries) == [
        True,
        True,
        True,
    ]


def test_all_disconnected(sol):
    n = 5
    nums = [1, 5, 9, 13, 17]
    max_diff = 2
    queries = [
        [0, 1],
        [1, 2],
        [2, 4],
        [3, 3],
    ]

    assert sol.pathExistenceQueries(n, nums, max_diff, queries) == [
        False,
        False,
        False,
        True,
    ]


def test_multiple_components(sol):
    n = 7
    nums = [1, 2, 3, 10, 11, 20, 21]
    max_diff = 2

    queries = [
        [0, 2],  # same component
        [3, 4],  # same component
        [5, 6],  # same component
        [0, 3],  # different
        [2, 5],  # different
        [4, 6],  # different
    ]

    assert sol.pathExistenceQueries(n, nums, max_diff, queries) == [
        True,
        True,
        True,
        False,
        False,
        False,
    ]


def test_gap_equal_to_max_diff(sol):
    n = 4
    nums = [1, 3, 5, 7]
    max_diff = 2

    queries = [
        [0, 3],
        [1, 2],
    ]

    # Difference == maxDiff should remain connected.
    assert sol.pathExistenceQueries(n, nums, max_diff, queries) == [
        True,
        True,
    ]


def test_empty_queries(sol):
    n = 3
    nums = [1, 2, 3]
    max_diff = 1

    assert sol.pathExistenceQueries(n, nums, max_diff, []) == []


@pytest.mark.parametrize(
    "nums,max_diff,queries,expected",
    [
        (
            [1, 2, 10, 11],
            2,
            [[0, 1], [2, 3], [1, 2]],
            [True, True, False],
        ),
        (
            [1, 4, 7],
            3,
            [[0, 2], [0, 1]],
            [True, True],
        ),
        (
            [1, 5, 6, 10],
            2,
            [[1, 2], [0, 3], [2, 3]],
            [True, False, False],
        ),
    ],
)
def test_parametrized(sol, nums, max_diff, queries, expected):
    assert (
        sol.pathExistenceQueries(
            len(nums),
            nums,
            max_diff,
            queries,
        )
        == expected
    )
