from lc_3063_linked_list_frequency import Solution, ListNode


head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, ListNode(2, ListNode(3, ListNode(1))))))))


def test_frequencies_of_elements():
    rv = Solution.frequencies_of_elements(head)
    assert rv.val == 3
    assert rv.next.val == 3
    assert rv.next.next.val == 2
