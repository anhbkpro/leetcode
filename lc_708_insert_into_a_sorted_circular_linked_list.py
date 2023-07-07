from lc_705_design_hashset import Node


def insert(head: Node, insertVal: int) -> Node:

    if head is None:
        new_node = Node(insertVal, None)
        new_node.next = new_node
        return new_node

    prev, curr = head, head.next
    to_insert = False

    while True:

        if prev.value <= insertVal <= curr.value:
            # Case #1.
            to_insert = True
        elif prev.value > curr.value:
            # Case #2. where we locate the tail element
            # 'prev' points to the tail, i.e. the largest element!
            if insertVal >= prev.value or insertVal <= curr.value:
                to_insert = True

        if to_insert:
            prev.next = Node(insertVal, curr)
            # mission accomplished
            return head

        prev, curr = curr, curr.next
        # loop condition
        if prev == head:
            break
    # Case #3.
    # did not insert the node in the loop
    prev.next = Node(insertVal, curr)
    return head


class Solution:
    pass
