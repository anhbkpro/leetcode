from lc_369_plus_one_linked_list import plusOne
from lc_61_rotate_list import ListNode


def test_plus_one():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    res = plusOne(head)
    assert f"{res.val} -> {res.next.val} -> {res.next.next.val}" == "1 -> 2 -> 4"
