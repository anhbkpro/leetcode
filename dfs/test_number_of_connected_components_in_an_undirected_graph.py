import pytest
from dfs.number_of_connected_components_in_an_undirected_graph import Solution


class TestCountComponents:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        assert solution.countComponents(n, edges) == 2

    def test_example2(self, solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2, 3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        assert solution.countComponents(n, edges) == 1

    def test_no_edges(self, solution):
        # Input: n = 4, edges = []
        # Output: 4
        # Explanation: Four components: {0}, {1}, {2}, {3}
        n = 4
        edges = []
        assert solution.countComponents(n, edges) == 4

    def test_single_node(self, solution):
        # Input: n = 1, edges = []
        # Output: 1
        # Explanation: One component: {0}
        n = 1
        edges = []
        assert solution.countComponents(n, edges) == 1

    def test_empty_graph(self, solution):
        # Input: n = 0, edges = []
        # Output: 0
        # Explanation: Zero components
        n = 0
        edges = []
        assert solution.countComponents(n, edges) == 0

    def test_multiple_components(self, solution):
        # Input: n = 6, edges = [[0, 1], [2, 3], [4, 5]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2, 3}, {4, 5}
        n = 6
        edges = [[0, 1], [2, 3], [4, 5]]
        assert solution.countComponents(n, edges) == 3

    def test_nodes_not_in_edges(self, solution):
        # Input: n = 4, edges = [[0, 1]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2}, {3}
        n = 4
        edges = [[0, 1]]
        assert solution.countComponents(n, edges) == 3

    def test_graph_with_cycle(self, solution):
        # Input: n = 4, edges = [[0, 1], [1, 2], [2, 0], [3, 3]] (self-loop ignored)
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3}
        n = 4
        edges = [[0, 1], [1, 2], [2, 0], [3, 3]]  # Self-loop [3, 3] is valid input
        assert solution.countComponents(n, edges) == 2  # DFS handles cycles

    def test_fully_connected_graph(self, solution):
        # Input: n = 3, edges = [[0, 1], [1, 2], [0, 2]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2}
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        assert solution.countComponents(n, edges) == 1

    def test_larger_graph(self, solution):
        # Input: n = 7, edges = [[0,1], [0,2], [1,3], [4,5]]
        # Output: 3
        # Explanation: Three components: {0, 1, 2, 3}, {4, 5}, {6}
        n = 7
        edges = [[0, 1], [0, 2], [1, 3], [4, 5]]
        assert solution.countComponents(n, edges) == 3
