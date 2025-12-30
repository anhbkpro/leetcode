from .linked_list_node import LinkedListNode
from .split_linked_list_in_parts import Solution


def test_split_linked_list_in_parts():
    # Input: head = [1,2,3], k = 5
    # Output: [[1],[2],[3],[],[]]
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    result = Solution().splitListToParts(head, 5)
    assert result[0].val == 1
    assert result[1].val == 2
    assert result[2].val == 3
    assert result[3] is None
    assert result[4] is None
