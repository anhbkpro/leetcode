from lc_141_linked_list_cycle import Solution, ListNode

head = [3, 2, 0, -4]
pos = 1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

node = node1


def test_has_cycle():
    assert Solution.hasCycle(head=ListNode(1)) is False
    assert Solution.hasCycle(head=node) is True
