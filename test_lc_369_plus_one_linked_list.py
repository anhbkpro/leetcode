from lc_369_plus_one_linked_list import Solution
from lc_61_rotate_list import ListNode


def test_plus_one():
    # test case 1: 123 -> 124
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    res = Solution.plus_one(head)
    assert f"{res}" == "[1, 2, 4]"

    # test case 2: 192999 -> 193000
    head = ListNode(1)
    head.next = ListNode(9)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(9)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(9)
    res = Solution.plus_one(head)
    assert f"{res}" == "[1, 9, 3, 0, 0, 0]"

    # test case 3: 999 -> 1000
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    res = Solution.plus_one(head)
    assert f"{res}" == "[1, 0, 0, 0]"
