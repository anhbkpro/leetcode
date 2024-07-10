from .remove_duplicates_from_an_unsorted_linked_list import Solution
from .linked_list_node import LinkedListNode


def test_remove_duplicates_from_an_unsorted_linked_list():
    # head = [1,2,3,2]
    # Output: [1,3]
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(2)
    expected = LinkedListNode(1)
    expected.next = LinkedListNode(3)
    solution = Solution()
    actual = solution.deleteDuplicatesUnsorted(head)
    assert are_equal(actual, expected)

    # head = [2,1,1,2]
    # Output: []
    head = LinkedListNode(2)
    head.next = LinkedListNode(1)
    head.next.next = LinkedListNode(1)
    head.next.next.next = LinkedListNode(2)
    expected = None
    solution = Solution()
    actual = solution.deleteDuplicatesUnsorted(head)
    assert are_equal(actual, expected)

    # head = [3,2,2,1,3,2,4]
    # Output: [1,4]
    head = LinkedListNode(3)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(2)
    head.next.next.next = LinkedListNode(1)
    head.next.next.next.next = LinkedListNode(3)
    head.next.next.next.next.next = LinkedListNode(2)
    head.next.next.next.next.next.next = LinkedListNode(4)
    expected = LinkedListNode(1)
    expected.next = LinkedListNode(4)
    solution = Solution()
    actual = solution.deleteDuplicatesUnsorted(head)
    assert are_equal(actual, expected)

def are_equal(head1: LinkedListNode, head2: LinkedListNode) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None
