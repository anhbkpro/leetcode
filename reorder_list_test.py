from reorder_list import Solution, ListNode


def test_reorder_list():
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(head)
    assert head.val == 1
    assert head.next.val == 5
    assert head.next.next.val == 2
    assert head.next.next.next.val == 4
    assert head.next.next.next.next.val == 3
    assert head.next.next.next.next.next is None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(head)
    assert head.val == 1
    assert head.next.val == 4
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
    assert head.next.next.next.next is None
    head = ListNode(1, ListNode(2, ListNode(3)))
    s.reorderList(head)
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 2
    assert head.next.next.next is None
    head = ListNode(1, ListNode(2))
    s.reorderList(head)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next is None
    head = ListNode(1)
    s.reorderList(head)
    assert head.val == 1
    assert head.next is None
