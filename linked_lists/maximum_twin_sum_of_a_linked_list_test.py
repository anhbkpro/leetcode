import unittest

from linked_lists.maximum_twin_sum_of_a_linked_list import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


class TestMaximumTwinSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        head = build_linked_list([5, 4, 2, 1])
        self.assertEqual(self.sol.pairSum(head), 6)

    def test_even_length(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(self.sol.pairSum(head), 7)

    def test_all_same(self):
        head = build_linked_list([3, 3, 3, 3])
        self.assertEqual(self.sol.pairSum(head), 6)

    def test_two_nodes(self):
        head = build_linked_list([1, 100])
        self.assertEqual(self.sol.pairSum(head), 101)

    def test_large_values(self):
        head = build_linked_list([1000, 2000, 3000, 4000])
        self.assertEqual(self.sol.pairSum(head), 5000)


if __name__ == "__main__":
    unittest.main()
