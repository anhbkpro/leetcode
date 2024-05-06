from linked_lists.remove_nodes_from_linked_list import ListNode, Solution


def test_remove_nodes_from_linked_list():
    # Input: head = [5,2,13,3,8]
    # Output: [13,8]
    head = ListNode(5)
    head.next = ListNode(2)
    head.next.next = ListNode(13)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)
    rv = Solution().removeNodes(head)
    assert rv.val == 13
    assert rv.next.val == 8
