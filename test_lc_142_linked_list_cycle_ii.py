from lc_141_linked_list_cycle import ListNode
from lc_142_linked_list_cycle_ii import Solution


def test_detect_cycle():
    assert Solution.detectCycle(head=None) is None
    assert Solution.detectCycle(head=ListNode(1)) is None
    head = ListNode(1)
    head.next = head
    assert Solution.detectCycle(head=head) == head

