from lc_19_remove_nth_node_from_end_of_list import Solution, ListNode


def test_remove_nth_from_end():
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rv = Solution.remove_nth_from_end(root, 2)
    assert rv.val == 1
    assert rv.next.val == 2
    assert rv.next.next.val == 3
    assert rv.next.next.next.val == 5
