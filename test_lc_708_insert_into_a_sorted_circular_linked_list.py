from lc_708_insert_into_a_sorted_circular_linked_list import insert
from lc_705_design_hashset import Node


def test_insert():
    head = Node(3, None)
    head.next = Node(4, None)
    head.next.next = Node(1, None)
    head.next.next.next = head
    res = insert(head, 2)
    assert f"{res.value} -> {res.next.value} -> {res.next.next.value} -> {res.next.next.next.value}" == "3 -> 4 -> 1 " \
                                                                                                        "-> 2"
