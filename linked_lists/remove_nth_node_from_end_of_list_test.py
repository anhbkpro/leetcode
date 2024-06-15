from .remove_nth_node_from_end_of_list import Solution, ListNode


def test_removeNthFromEnd():
    solution = Solution()

    # Example 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    result = solution.removeNthFromEnd(head, n)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 5

    # Example 2
    head = ListNode(1)
    n = 1
    result = solution.removeNthFromEnd(head, n)
    assert result is None
