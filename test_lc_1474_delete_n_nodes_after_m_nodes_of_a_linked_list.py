from lc_1474_delete_n_nodes_after_m_nodes_of_a_linked_list import deleteNodes
from lc_61_rotate_list import ListNode

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
m = 2
n = 3


def test_delete_nodes():
    result = f"{deleteNodes(head, m, n)}"
    assert result == "[1, 2, 6]"
