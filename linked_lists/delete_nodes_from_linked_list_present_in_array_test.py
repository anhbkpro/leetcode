from .delete_nodes_from_linked_list_present_in_array import Solution
from .linked_list_node import LinkedListNode


def test_delete_nodes_from_linked_list_present_in_array():
    # Input: nums = [1,2,3], head = [1,2,3,4,5]
    # Output: [4,5]
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(4)
    head.next.next.next.next = LinkedListNode(5)
    head = Solution().modifiedList([1, 2, 3], head)
    assert head.val == 4
    assert head.next.val == 5
