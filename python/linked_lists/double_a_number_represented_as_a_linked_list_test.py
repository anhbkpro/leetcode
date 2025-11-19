from .double_a_number_represented_as_a_linked_list import Solution
from .linked_list_node import LinkedListNode


def test_double_a_number_represented_as_a_linked_list():
    # Input: head = [1,8,9]
    # Output: [3,7,8]
    head = LinkedListNode(1)
    head.next = LinkedListNode(8)
    head.next.next = LinkedListNode(9)
    rv = Solution().doubleIt(head)
    assert rv.val == 3
    assert rv.next.val == 7
    assert rv.next.next.val == 8
    assert rv.next.next.next is None

    # Input: head = [9,9,9]
    # Output: [1,9,9,8]
    head = LinkedListNode(9)
    head.next = LinkedListNode(9)
    head.next.next = LinkedListNode(9)
    rv = Solution().doubleIt(head)
    assert rv.val == 1
    assert rv.next.val == 9
    assert rv.next.next.val == 9
    assert rv.next.next.next.val == 8
    assert rv.next.next.next.next is None
