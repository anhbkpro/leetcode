import unittest

from linked_lists.linked_list_cycle import (
    ListNode,
    SolutionFloydCycle,
    SolutionHashTable,
)


class LinkedListCycleTest:
    """Base test class for LinkedListCycle problem."""

    def create_linked_list(self, values, pos=-1):
        """
        Helper method to create a linked list with an optional cycle.

        Args:
            values: List of values to create nodes
            pos: Position to create cycle (-1 means no cycle)

        Returns:
            Head of the linked list
        """
        if not values:
            return None

        # Create nodes
        nodes = [ListNode(val) for val in values]

        # Link nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Create cycle if pos is valid
        if pos >= 0 and pos < len(nodes):
            nodes[-1].next = nodes[pos]

        return nodes[0]

    def test_example_1(self):
        # Test case from LeetCode example 1: [3,2,0,-4], pos = 1
        head = self.create_linked_list([3, 2, 0, -4], pos=1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_example_2(self):
        # Test case from LeetCode example 2: [1,2], pos = 0
        head = self.create_linked_list([1, 2], pos=0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_example_3(self):
        # Test case from LeetCode example 3: [1], pos = -1
        head = self.create_linked_list([1], pos=-1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_empty_list(self):
        # Test with empty list
        self.assertFalse(self.solution.hasCycle(None))

    def test_single_node_with_self_cycle(self):
        # Test single node pointing to itself
        node = ListNode(1)
        node.next = node
        self.assertTrue(self.solution.hasCycle(node))

    def test_two_nodes_no_cycle(self):
        # Test two nodes without cycle
        head = self.create_linked_list([1, 2])
        self.assertFalse(self.solution.hasCycle(head))

    def test_multiple_nodes_cycle_at_end(self):
        # Test multiple nodes with cycle at the end
        head = self.create_linked_list([1, 2, 3, 4, 5], pos=4)
        self.assertTrue(self.solution.hasCycle(head))

    def test_multiple_nodes_no_cycle(self):
        # Test multiple nodes without cycle
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertFalse(self.solution.hasCycle(head))


class TestLinkedListCycleHashTable(unittest.TestCase, LinkedListCycleTest):
    """Test cases for hash table-based solution."""

    def setUp(self):
        self.solution = SolutionHashTable()


class TestLinkedListCycleFloyd(unittest.TestCase, LinkedListCycleTest):
    """Test cases for Floyd's cycle finding algorithm solution."""

    def setUp(self):
        self.solution = SolutionFloydCycle()


if __name__ == "__main__":
    unittest.main()
