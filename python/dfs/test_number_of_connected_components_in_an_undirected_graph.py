import pytest

from dfs.number_of_connected_components_in_an_undirected_graph import DFS, UnionFind


class TestCountComponents:
    @pytest.fixture
    def dfs_solution(self):
        return DFS()

    @pytest.fixture
    def union_find_solution(self):
        return UnionFind()

    def test_example1_dfs(self, dfs_solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        assert dfs_solution.countComponents(n, edges) == 2

    def test_example1_union_find(self, union_find_solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        assert union_find_solution.countComponents(n, edges) == 2

    def test_example2_dfs(self, dfs_solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2, 3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        assert dfs_solution.countComponents(n, edges) == 1

    def test_example2_union_find(self, union_find_solution):
        # Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2, 3, 4}
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        assert union_find_solution.countComponents(n, edges) == 1

    def test_no_edges_dfs(self, dfs_solution):
        # Input: n = 4, edges = []
        # Output: 4
        # Explanation: Four components: {0}, {1}, {2}, {3}
        n = 4
        edges = []
        assert dfs_solution.countComponents(n, edges) == 4

    def test_no_edges_union_find(self, union_find_solution):
        # Input: n = 4, edges = []
        # Output: 4
        # Explanation: Four components: {0}, {1}, {2}, {3}
        n = 4
        edges = []
        assert union_find_solution.countComponents(n, edges) == 4

    def test_single_node_dfs(self, dfs_solution):
        # Input: n = 1, edges = []
        # Output: 1
        # Explanation: One component: {0}
        n = 1
        edges = []
        assert dfs_solution.countComponents(n, edges) == 1

    def test_single_node_union_find(self, union_find_solution):
        # Input: n = 1, edges = []
        # Output: 1
        # Explanation: One component: {0}
        n = 1
        edges = []
        assert union_find_solution.countComponents(n, edges) == 1

    def test_empty_graph_dfs(self, dfs_solution):
        # Input: n = 0, edges = []
        # Output: 0
        # Explanation: Zero components
        n = 0
        edges = []
        assert dfs_solution.countComponents(n, edges) == 0

    def test_empty_graph_union_find(self, union_find_solution):
        # Input: n = 0, edges = []
        # Output: 0
        # Explanation: Zero components
        n = 0
        edges = []
        assert union_find_solution.countComponents(n, edges) == 0

    def test_multiple_components_dfs(self, dfs_solution):
        # Input: n = 6, edges = [[0, 1], [2, 3], [4, 5]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2, 3}, {4, 5}
        n = 6
        edges = [[0, 1], [2, 3], [4, 5]]
        assert dfs_solution.countComponents(n, edges) == 3

    def test_multiple_components_union_find(self, union_find_solution):
        # Input: n = 6, edges = [[0, 1], [2, 3], [4, 5]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2, 3}, {4, 5}
        n = 6
        edges = [[0, 1], [2, 3], [4, 5]]
        assert union_find_solution.countComponents(n, edges) == 3

    def test_nodes_not_in_edges_dfs(self, dfs_solution):
        # Input: n = 4, edges = [[0, 1]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2}, {3}
        n = 4
        edges = [[0, 1]]
        assert dfs_solution.countComponents(n, edges) == 3

    def test_nodes_not_in_edges_union_find(self, union_find_solution):
        # Input: n = 4, edges = [[0, 1]]
        # Output: 3
        # Explanation: Three components: {0, 1}, {2}, {3}
        n = 4
        edges = [[0, 1]]
        assert union_find_solution.countComponents(n, edges) == 3

    def test_graph_with_cycle_dfs(self, dfs_solution):
        # Input: n = 4, edges = [[0, 1], [1, 2], [2, 0], [3, 3]] (self-loop ignored)
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3}
        n = 4
        edges = [[0, 1], [1, 2], [2, 0], [3, 3]]  # Self-loop [3, 3] is valid input
        assert dfs_solution.countComponents(n, edges) == 2  # DFS handles cycles

    def test_graph_with_cycle_union_find(self, union_find_solution):
        # Input: n = 4, edges = [[0, 1], [1, 2], [2, 0], [3, 3]] (self-loop ignored)
        # Output: 2
        # Explanation: Two components: {0, 1, 2} and {3}
        n = 4
        edges = [[0, 1], [1, 2], [2, 0], [3, 3]]  # Self-loop [3, 3] is valid input
        assert (
            union_find_solution.countComponents(n, edges) == 2
        )  # UnionFind handles cycles

    def test_fully_connected_graph_dfs(self, dfs_solution):
        # Input: n = 3, edges = [[0, 1], [1, 2], [0, 2]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2}
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        assert dfs_solution.countComponents(n, edges) == 1

    def test_fully_connected_graph_union_find(self, union_find_solution):
        # Input: n = 3, edges = [[0, 1], [1, 2], [0, 2]]
        # Output: 1
        # Explanation: Single component: {0, 1, 2}
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        assert union_find_solution.countComponents(n, edges) == 1

    def test_larger_graph_dfs(self, dfs_solution):
        # Input: n = 7, edges = [[0,1], [0,2], [1,3], [4,5]]
        # Output: 3
        # Explanation: Three components: {0, 1, 2, 3}, {4, 5}, {6}
        n = 7
        edges = [[0, 1], [0, 2], [1, 3], [4, 5]]
        assert dfs_solution.countComponents(n, edges) == 3

    def test_larger_graph_union_find(self, union_find_solution):
        # Input: n = 7, edges = [[0,1], [0,2], [1,3], [4,5]]
        # Output: 3
        # Explanation: Three components: {0, 1, 2, 3}, {4, 5}, {6}
        n = 7
        edges = [[0, 1], [0, 2], [1, 3], [4, 5]]
        assert union_find_solution.countComponents(n, edges) == 3

    def test_complex_graph_dfs(self, dfs_solution):
        # Input: n = 10, edges = [[0,1], [1,2], [2,3], [3,4], [5,6], [6,7], [8,9]]
        # Output: 3
        # Explanation: Three components: {0,1,2,3,4}, {5,6,7}, {8,9}
        n = 10
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [8, 9]]
        assert dfs_solution.countComponents(n, edges) == 3

    def test_complex_graph_union_find(self, union_find_solution):
        # Input: n = 10, edges = [[0,1], [1,2], [2,3], [3,4], [5,6], [6,7], [8,9]]
        # Output: 3
        # Explanation: Three components: {0,1,2,3,4}, {5,6,7}, {8,9}
        n = 10
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [8, 9]]
        assert union_find_solution.countComponents(n, edges) == 3

    def test_compare_implementations(self):
        # Test that both implementations give the same results for various inputs
        dfs = DFS()
        uf = UnionFind()

        test_cases = [
            (5, [[0, 1], [1, 2], [3, 4]]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
            (4, []),
            (1, []),
            (0, []),
            (6, [[0, 1], [2, 3], [4, 5]]),
            (4, [[0, 1]]),
            (4, [[0, 1], [1, 2], [2, 0], [3, 3]]),
            (3, [[0, 1], [1, 2], [0, 2]]),
            (7, [[0, 1], [0, 2], [1, 3], [4, 5]]),
            (10, [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [8, 9]]),
        ]

        for n, edges in test_cases:
            dfs_result = dfs.countComponents(n, edges)
            uf_result = uf.countComponents(n, edges)
            assert (
                dfs_result == uf_result
            ), f"DFS: {dfs_result}, UnionFind: {uf_result} for n={n}, edges={edges}"
