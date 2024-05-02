from linked_lists.delete_the_middle_node_of_a_linked_list import Solution, ListNode


def test_delete_the_middle_node_of_a_linked_list():
    # head = [1,3,4,7,1,2,6]
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(6)
    Solution().deleteMiddle(head.next.next)
    assert head.val == 1
