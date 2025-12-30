from linked_lists.linked_list_node import LinkedListNode

from .linked_list_cycle import Solution


def test_linked_list_cycle():
    node = LinkedListNode(3)
    node.next = LinkedListNode(2)
    node.next.next = LinkedListNode(0)
    node.next.next.next = LinkedListNode(-4)
    node.next.next.next.next = node.next
    assert Solution().hasCycle(node) == True

    node = LinkedListNode(1)
    node.next = LinkedListNode(2)
    node.next.next = node
    assert Solution().hasCycle(node) == True
