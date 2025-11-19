from .delete_the_middle_node_of_a_linked_list import Solution
from .linked_list_node import LinkedListNode


def test_delete_the_middle_node_of_a_linked_list():
    # head = [1,3,4,7,1,2,6]
    head = LinkedListNode(1)
    head.next = LinkedListNode(3)
    head.next.next = LinkedListNode(4)
    head.next.next.next = LinkedListNode(7)
    head.next.next.next.next = LinkedListNode(1)
    head.next.next.next.next.next = LinkedListNode(2)
    head.next.next.next.next.next.next = LinkedListNode(6)
    Solution().deleteMiddle(head.next.next)
    assert head.val == 1
