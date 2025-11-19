import unittest
from typing import List, Optional
from linked_lists.add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(unittest.TestCase):
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
        # l1 = [2,4,3], l2 = [5,6,4]
        # Expected: [7,0,8] (342 + 465 = 807)
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 8])

    def test_example_2(self):
        # Test case from LeetCode example 2
        # l1 = [0], l2 = [0]
        # Expected: [0]
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0])

    def test_example_3(self):
        # Test case from LeetCode example 3
        # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        # Expected: [8,9,9,9,0,0,0,1]
        l1 = self.create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.create_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_different_lengths(self):
        # Test with numbers of different lengths
        # 12 + 789 = 801
        l1 = self.create_linked_list([2, 1])
        l2 = self.create_linked_list([9, 8, 7])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [1, 0, 8])

    def test_carry_propagation(self):
        # Test carry propagation
        # 999 + 1 = 1000
        l1 = self.create_linked_list([9, 9, 9])
        l2 = self.create_linked_list([1])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 0, 0, 1])

    def test_single_digit_with_carry(self):
        # Test single digit addition with carry
        # 5 + 5 = 10
        l1 = self.create_linked_list([5])
        l2 = self.create_linked_list([5])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 1])

    def test_large_numbers(self):
        # Test with large numbers
        # 1000000 + 234567 = 1234567
        l1 = self.create_linked_list([0, 0, 0, 0, 0, 0, 1])
        l2 = self.create_linked_list([7, 6, 5, 4, 3, 2])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
