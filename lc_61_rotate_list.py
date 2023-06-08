# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Convert linked list to a list
    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return str(result)


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Time complexity: O(N)
    Space complexity: O(1)
    """
    # base cases
    if not head:
        return None
    if not head.next:
        return head

    # close the linked list into the ring
    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head

    # find new tail : (n - k % n - 1)th node
    # and new head : (n - k % n)th node
    new_tail = head
    for i in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # break the ring
    new_tail.next = None

    return new_head


class Solution:
    pass
