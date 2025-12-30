from .linked_list_node import LinkedListNode
from .spiral_matrix_iv import Solution


def test_spiral_matrix():
    head = LinkedListNode(0)
    head.next = LinkedListNode(1)
    head.next.next = LinkedListNode(2)
    assert Solution().spiralMatrix(m=1, n=4, head=head) == [[0, 1, 2, -1]]
