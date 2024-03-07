from lc_876_middle_of_the_linked_list import Solution, ListNode

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


def test_middle_node():
    assert Solution.middle_node(head=head).val == 3
