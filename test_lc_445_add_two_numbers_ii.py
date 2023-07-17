from lc_445_add_two_numbers_ii import add_two_numbers, ListNode


head = ListNode(7)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)


def test_add_two_numbers():
    assert add_two_numbers(head, head2).val == 7
    assert add_two_numbers(head, head2).next.val == 8
    assert add_two_numbers(head, head2).next.next.val == 0
    assert add_two_numbers(head, head2).next.next.next.val == 7

