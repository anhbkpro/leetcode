from linked_lists.middle_of_the_linked_list import Solution, ListNode


def test_middle_of_the_linked_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    assert Solution().middleNode(head).val == 3
