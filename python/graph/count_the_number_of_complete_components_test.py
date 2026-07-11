import pytest

from .count_the_number_of_complete_components import Solution


@pytest.fixture
def sol():
    return Solution()


def test_single_complete_component(sol):
    # Test case with one complete component (triangle)
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    expected = 1  # One complete component where all vertices are connected
    assert sol.countCompleteComponents(n, edges) == expected


def test_multiple_complete_components(sol):
    # Test case with multiple complete components
    n = 6
    edges = [
        [0, 1],
        [1, 2],
        [2, 0],  # Complete triangle
        [3, 4],
        [4, 5],
        [5, 3],  # Another complete triangle
    ]
    expected = 2  # Two complete components
    assert sol.countCompleteComponents(n, edges) == expected


def test_no_complete_components(sol):
    # Test case with no complete components
    n = 4
    edges = [[0, 1], [1, 2], [2, 3]]  # Line graph
    expected = 0  # No complete components
    assert sol.countCompleteComponents(n, edges) == expected


def test_isolated_vertices(sol):
    # Test case with isolated vertices
    n = 5
    edges = [[0, 1], [1, 0]]  # One edge and three isolated vertices
    expected = 3  # Three isolated vertices are complete components
    assert sol.countCompleteComponents(n, edges) == expected


def test_empty_graph(sol):
    # Test case with no edges
    n = 3
    edges = []
    expected = 3  # All vertices are isolated and thus complete components
    assert sol.countCompleteComponents(n, edges) == expected


def test_single_vertex(sol):
    # Test case with just one vertex
    n = 1
    edges = []
    expected = 1  # Single vertex is a complete component
    assert sol.countCompleteComponents(n, edges) == expected


def test_mixed_components(sol):
    # Test case with mix of complete and incomplete components
    n = 7
    edges = [
        [0, 1],
        [1, 2],
        [2, 0],  # Complete triangle
        [3, 4],
        [4, 5],  # Incomplete component
        # Vertex 6 is isolated
    ]
    expected = 2  # One complete triangle and one isolated vertex
    assert sol.countCompleteComponents(n, edges) == expected


def test_complete_pairs(sol):
    # Test case with multiple complete pairs
    n = 6
    edges = [[0, 1], [2, 3], [4, 5]]  # Three complete pairs
    expected = 3  # Three complete components of size 2
    assert sol.countCompleteComponents(n, edges) == expected
