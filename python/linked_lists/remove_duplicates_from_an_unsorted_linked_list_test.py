from .linked_list import LinkedList
from .linked_list_node import LinkedListNode
from .remove_duplicates_from_an_unsorted_linked_list import Solution


def test_remove_duplicates_from_an_unsorted_linked_list():
    # head = [1,2,3,2]
    # Output: [1,3]
    actual = LinkedList()
    actual.create_linked_list([1, 2, 3, 2])
    head = actual.head
    expected = LinkedList()
    expected.create_linked_list([1, 3])
    actual = Solution().deleteDuplicatesUnsorted(head)
    assert are_equal(actual, expected.head)

    # head = [2,1,1,2]
    # Output: []
    actual = LinkedList()
    actual.create_linked_list([2, 1, 1, 2])
    head = actual.head
    expected = None
    actual = Solution().deleteDuplicatesUnsorted(head)
    assert actual == expected

    # head = [3,2,2,1,3,2,4]
    # Output: [1,4]
    actual = LinkedList()
    actual.create_linked_list([3, 2, 2, 1, 3, 2, 4])
    head = actual.head
    expected = LinkedList()
    expected.create_linked_list([1, 4])
    actual = Solution().deleteDuplicatesUnsorted(head)
    assert are_equal(actual, expected.head)


def are_equal(head1: LinkedListNode, head2: LinkedListNode) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None
