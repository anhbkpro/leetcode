import unittest
from typing import List, Optional

from linked_lists.merge_two_sorted_lists import ListNode, Solution


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        """
        Helper method to create a linked list from a list of values.

        Args:
            values: List of integers to create nodes from

        Returns:
            Head of the linked list or None if values is empty
        """
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        """
        Helper method to convert a linked list to a list of values.

        Args:
            head: Head of the linked list

        Returns:
            List of values from the linked list
        """
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1(self):
        # Test case from LeetCode example 1
        # list1 = [1,2,4], list2 = [1,3,4]
        # Expected: [1,1,2,3,4,4]
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        # Test case from LeetCode example 2
        # list1 = [], list2 = []
        # Expected: []
        list1 = self.create_linked_list([])
        list2 = self.create_linked_list([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [])

    def test_example_3(self):
        # Test case from LeetCode example 3
        # list1 = [], list2 = [0]
        # Expected: [0]
        list1 = self.create_linked_list([])
        list2 = self.create_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [0])

    def test_different_lengths(self):
        # Test with lists of different lengths
        list1 = self.create_linked_list([1, 3, 5])
        list2 = self.create_linked_list([2, 4, 6, 8, 10])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5, 6, 8, 10])

    def test_one_empty_list(self):
        # Test when one list is empty
        list1 = self.create_linked_list([1, 2, 3])
        list2 = self.create_linked_list([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3])

    def test_duplicate_values(self):
        # Test with duplicate values
        list1 = self.create_linked_list([1, 1, 2, 3, 3])
        list2 = self.create_linked_list([1, 2, 2, 3])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_negative_numbers(self):
        # Test with negative numbers
        list1 = self.create_linked_list([-3, -1, 1])
        list2 = self.create_linked_list([-2, 0, 2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [-3, -2, -1, 0, 1, 2])

    def test_single_element_lists(self):
        # Test with single element lists
        list1 = self.create_linked_list([1])
        list2 = self.create_linked_list([2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 2])


if __name__ == "__main__":
    unittest.main()
