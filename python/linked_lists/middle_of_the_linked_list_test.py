from .linked_list_node import LinkedListNode
from .middle_of_the_linked_list import Solution


def test_middle_of_the_linked_list():
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(4)
    head.next.next.next.next = LinkedListNode(5)
    assert Solution().middleNode(head).val == 3
