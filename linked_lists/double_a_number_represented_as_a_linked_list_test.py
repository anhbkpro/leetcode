from linked_lists.double_a_number_represented_as_a_linked_list import ListNode, Solution


def test_double_a_number_represented_as_a_linked_list():
    # Input: head = [1,8,9]
    # Output: [3,7,8]
    head = ListNode(1)
    head.next = ListNode(8)
    head.next.next = ListNode(9)
    rv = Solution().doubleIt(head)
    assert rv.val == 3
    assert rv.next.val == 7
    assert rv.next.next.val == 8
    assert rv.next.next.next is None

    # Input: head = [9,9,9]
    # Output: [1,9,9,8]
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    rv = Solution().doubleIt(head)
    assert rv.val == 1
    assert rv.next.val == 9
    assert rv.next.next.val == 9
    assert rv.next.next.next.val == 8
    assert rv.next.next.next.next is None
