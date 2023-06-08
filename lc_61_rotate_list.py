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
    if not head:
        return None
    if not head.next:
        return head
    # find the length of the list
    length = 1
    old_tail = head
    while old_tail.next:
        length += 1
        old_tail = old_tail.next
    # connect the tail to the head
    old_tail.next = head
    # find the new tail
    new_tail = head
    for _ in range(length - k % length - 1):
        new_tail = new_tail.next
    # find the new head
    new_head = new_tail.next
    # break the ring
    new_tail.next = None
    return new_head


class Solution:
    pass
