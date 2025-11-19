from .delete_node_in_a_linked_list import Solution
from .linked_list_node import LinkedListNode


def test_delete_node_in_a_linked_list():
    # Input: head = [4,5,1,9], node = 5
    # Output: [4,1,9]
    head = LinkedListNode(4)
    head.next = LinkedListNode(5)
    head.next.next = LinkedListNode(1)
    head.next.next.next = LinkedListNode(9)
    node = head.next
    Solution().deleteNode(node)
    assert head.val == 4
    assert head.next.val == 1
    assert head.next.next.val == 9
