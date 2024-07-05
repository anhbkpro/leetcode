from .find_the_minimum_and_maximum_number_of_nodes_between_critical_points import Solution
from .linked_list_node import LinkedListNode


def test_nodes_between_critical_points():
    # head = [3,1]
    head = LinkedListNode(3)
    head.next = LinkedListNode(1)
    assert Solution().nodesBetweenCriticalPoints(head) == [-1, -1]

    # head = [5,3,1,2,5,1,2]
    head = LinkedListNode(5)
    head.next = LinkedListNode(3)
    head.next.next = LinkedListNode(1)
    head.next.next.next = LinkedListNode(2)
    head.next.next.next.next = LinkedListNode(5)
    head.next.next.next.next.next = LinkedListNode(1)
    head.next.next.next.next.next.next = LinkedListNode(2)
    assert Solution().nodesBetweenCriticalPoints(head) == [1, 3]
