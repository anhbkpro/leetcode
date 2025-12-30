from .linked_list_node import LinkedListNode
from .remove_nodes_from_linked_list import Solution


def test_remove_nodes_from_linked_list():
    # Input: head = [5,2,13,3,8]
    # Output: [13,8]
    head = LinkedListNode(5)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(13)
    head.next.next.next = LinkedListNode(3)
    head.next.next.next.next = LinkedListNode(8)
    rv = Solution().removeNodes(head)
    assert rv.val == 13
    assert rv.next.val == 8
