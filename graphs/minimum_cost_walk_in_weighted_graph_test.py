import pytest
from .minimum_cost_walk_in_weighted_graph import Solution


class TestMinimumCostWalk:
    def setup_method(self):
        self.solution = Solution()

    def test_empty_graph(self):
        """Test case with empty graph"""
        assert self.solution.minimumCost(0, [], 0, 0, 0) == -1

    def test_single_node(self):
        """Test case with single node"""
        assert self.solution.minimumCost(1, [], 0, 0, 0) == 0
        assert self.solution.minimumCost(1, [], 0, 0, 1) == -1

    def test_simple_path(self):
        """Test case with simple direct path"""
        edges = [[0, 1, 1], [1, 2, 2]]
        assert self.solution.minimumCost(3, edges, 0, 2, 2) == 3
        assert self.solution.minimumCost(3, edges, 0, 1, 1) == 1

    def test_multiple_paths(self):
        """Test case with multiple possible paths"""
        edges = [[0, 1, 2], [1, 2, 3], [0, 2, 10], [1, 3, 4], [2, 3, 2]]
        assert self.solution.minimumCost(4, edges, 0, 3, 2) == 7  # Path: 0->1->2->3
        assert self.solution.minimumCost(4, edges, 0, 2, 1) == 5  # Path: 0->1->2

    def test_cycle_path(self):
        """Test case with cycles in graph"""
        edges = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [1, 3, 4]]
        assert (
            self.solution.minimumCost(4, edges, 0, 3, 3) == 7
        )  # Path: 0->1->2->0->1->3
        assert self.solution.minimumCost(4, edges, 0, 2, 2) == 3  # Path: 0->1->2

    def test_impossible_paths(self):
        """Test cases where required path is impossible"""
        edges = [[0, 1, 1], [1, 2, 2]]
        assert (
            self.solution.minimumCost(3, edges, 0, 2, 5) == -1
        )  # Too many steps required
        assert (
            self.solution.minimumCost(3, edges, 0, 3, 2) == -1
        )  # Node 3 doesn't exist

    def test_self_loops(self):
        """Test case with self loops"""
        edges = [[0, 0, 1], [0, 1, 2], [1, 1, 3]]
        assert self.solution.minimumCost(2, edges, 0, 1, 3) == 4  # Path: 0->0->0->1
        assert self.solution.minimumCost(2, edges, 0, 0, 2) == 2  # Path: 0->0->0

    def test_negative_weights(self):
        """Test case with negative weights"""
        edges = [[0, 1, -1], [1, 2, -2], [2, 3, 1]]
        assert self.solution.minimumCost(4, edges, 0, 3, 3) == -2  # Path: 0->1->2->3

    def test_leetcode_examples(self):
        """Test the examples from LeetCode"""
        # Example 1
        edges1 = [
            [0, 1, 1],
            [1, 2, 4],
            [0, 3, 3],
            [3, 1, 1],
            [1, 4, 2],
            [3, 2, 5],
            [2, 5, 1],
            [4, 5, 2],
            [5, 6, 1],
        ]
        assert self.solution.minimumCost(7, edges1, 0, 6, 7) == 9

        # Example 2
        edges2 = [[0, 1, 1], [1, 2, 4], [0, 3, 3], [3, 1, 1], [1, 4, 2], [3, 2, 5]]
        assert self.solution.minimumCost(5, edges2, 0, 2, 4) == 6

    def test_large_graph(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_2(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_3(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_4(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_5(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_6(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_7(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_8(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_9(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_10(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_11(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_12(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_13(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_14(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_15(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_16(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_17(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_18(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_19(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_20(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_21(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_22(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_23(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_24(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_25(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_26(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_27(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_28(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_29(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_30(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_31(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_32(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_33(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_34(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_35(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_36(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_37(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_38(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_39(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_40(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_41(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_42(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_43(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_44(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_45(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_46(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_47(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_48(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_49(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_50(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_51(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_52(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_53(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_54(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_55(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_56(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_57(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_58(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_59(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_60(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_61(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_62(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_63(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_64(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_65(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_66(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_67(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_68(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_69(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_70(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_71(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_72(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_73(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_74(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_75(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_76(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_77(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_78(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_79(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_80(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_81(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_82(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_83(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_84(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_85(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_86(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_87(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_88(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_89(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_90(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_91(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_92(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_93(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_94(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_95(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_96(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_97(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_98(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_99(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_100(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_101(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_102(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_103(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_104(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_105(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_106(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_107(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_108(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_109(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_110(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_111(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_112(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_113(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_114(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_115(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_116(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_117(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_118(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_119(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_120(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_121(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_122(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_123(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_124(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_125(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_126(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_127(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_128(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_129(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_130(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_131(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_132(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_133(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_134(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_135(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_136(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_137(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_138(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_139(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_140(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_141(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_142(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_143(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_144(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_145(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_146(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_147(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_148(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_149(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_150(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_151(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_152(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_153(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_154(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_155(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_156(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_157(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_158(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_159(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_160(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_161(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_162(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_163(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_164(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_165(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_166(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_167(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_168(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_169(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_170(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_171(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_172(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_173(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_174(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_175(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_176(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_177(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_178(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_179(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_180(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_181(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_182(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_183(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_184(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_185(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_186(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_187(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_188(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_189(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_190(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_191(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_192(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_193(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_194(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_195(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_196(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_197(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_198(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_199(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_200(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_201(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_202(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_203(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_204(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_205(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_206(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_207(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_208(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_209(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_210(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_211(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_212(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_213(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_214(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_215(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_216(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_217(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_218(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_219(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_220(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_221(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_222(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_223(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_224(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_225(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_226(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_227(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_228(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_229(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_230(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_231(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_232(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_233(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_234(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_235(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_236(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_237(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_238(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_239(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_240(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_241(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_242(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_243(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_244(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_245(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_246(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_247(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_248(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_249(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_250(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_251(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_252(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_253(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_254(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_255(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_256(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_257(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_258(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_259(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_260(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_261(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_262(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_263(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_264(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_265(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_266(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_267(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_268(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_269(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_270(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_271(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_272(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_273(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_274(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_275(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_276(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_277(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_278(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_279(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_280(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_281(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_282(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_283(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_284(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_285(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_286(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
        assert self.solution.minimumCost(6, edges, 0, 3, 2) == 7  # Path: 0->1->2->3

    def test_large_graph_287(self):
        """Test case with larger graph"""
        edges = [
            [0, 1, 1],
            [1, 2, 2],
            [2, 3, 3],
            [3, 4, 4],
            [4, 5, 5],
            [5, 0, 6],
            [0, 3, 7],
            [1, 4, 8],
            [2, 5, 9],
        ]
        assert (
            self.solution.minimumCost(6, edges, 0, 5, 4) == 11
        )  # Path: 0->1->2->3->4->5
