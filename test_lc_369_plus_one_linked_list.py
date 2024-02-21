from lc_369_plus_one_linked_list import Solution
from lc_61_rotate_list import ListNode


def test_plus_one():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    res = Solution.plus_one(head)
    assert f"{res}" == "[1, 2, 4]"
