import unittest

from linked_lists.copy_list_with_random_pointer import Node, Solution


class TestCopyRandomList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_nodes(self, values, random_indices):
        """
        Helper method to create a linked list with random pointers.

        Args:
            values: List of values for nodes
            random_indices: List of indices for random pointers (-1 means None)

        Returns:
            Head of the created linked list
        """
        if not values:
            return None

        # Create nodes first
        nodes = [Node(val) for val in values]

        # Connect next pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Connect random pointers
        for i, random_idx in enumerate(random_indices):
            nodes[i].random = nodes[random_idx] if random_idx != -1 else None

        return nodes[0]

    def verify_lists_equal(self, original, copied):
        """
        Helper method to verify that two lists are equal in structure and values,
        but are different objects.

        Args:
            original: Head of original list
            copied: Head of copied list

        Returns:
            True if lists are equal but different objects
        """
        # Create maps to store node relationships
        original_to_copy = {}
        ptr_original = original
        ptr_copy = copied

        # First pass: verify values and next pointers, build node mapping
        while ptr_original and ptr_copy:
            # Verify different objects
            self.assertNotEqual(id(ptr_original), id(ptr_copy))
            # Verify values are equal
            self.assertEqual(ptr_original.val, ptr_copy.val)
            # Store mapping
            original_to_copy[ptr_original] = ptr_copy
            ptr_original = ptr_original.next
            ptr_copy = ptr_copy.next

        # Verify both lists ended
        self.assertIsNone(ptr_original)
        self.assertIsNone(ptr_copy)

        # Second pass: verify random pointers
        ptr_original = original
        while ptr_original:
            if ptr_original.random:
                self.assertEqual(
                    original_to_copy[ptr_original].random,
                    original_to_copy[ptr_original.random],
                )
            else:
                self.assertIsNone(original_to_copy[ptr_original].random)
            ptr_original = ptr_original.next

    def test_example_1(self):
        # Test case from LeetCode example 1
        # [[7,null],[13,0],[11,4],[10,2],[1,0]]
        head = self.create_nodes([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_example_2(self):
        # Test case from LeetCode example 2
        # [[1,1],[2,1]]
        head = self.create_nodes([1, 2], [1, 1])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_example_3(self):
        # Test case from LeetCode example 3
        # [[3,null],[3,0],[3,null]]
        head = self.create_nodes([3, 3, 3], [-1, 0, -1])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_empty_list(self):
        # Test with empty list
        head = None
        copied = self.solution.copyRandomList(head)
        self.assertIsNone(copied)

    def test_single_node(self):
        # Test with single node pointing to itself
        head = self.create_nodes([1], [0])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_all_random_none(self):
        # Test when all random pointers are None
        head = self.create_nodes([1, 2, 3], [-1, -1, -1])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_circular_random(self):
        # Test with circular random pointers
        head = self.create_nodes([1, 2, 3, 4], [1, 2, 3, 0])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)

    def test_same_random(self):
        # Test when multiple nodes point to the same random node
        head = self.create_nodes([1, 2, 3, 4], [1, 1, 1, 1])
        copied = self.solution.copyRandomList(head)
        self.verify_lists_equal(head, copied)


if __name__ == "__main__":
    unittest.main()
