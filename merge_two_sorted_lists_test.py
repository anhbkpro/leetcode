from merge_two_sorted_lists import Solution, ListNode


def test_mergeTwoLists():
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    result = s.mergeTwoLists(l1, l2)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4


