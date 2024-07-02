from .remove_nth_node_from_end_of_list import Solution
from .linked_list_node import LinkedListNode


def test_removeNthFromEnd():
    solution = Solution()

    # Example 1
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(4)
    head.next.next.next.next = LinkedListNode(5)
    n = 2
    result = solution.removeNthFromEnd(head, n)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 5

    # Example 2
    head = LinkedListNode(1)
    n = 1
    result = solution.removeNthFromEnd(head, n)
    assert result is None
