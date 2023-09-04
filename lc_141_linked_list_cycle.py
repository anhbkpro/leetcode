# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head  # move one step
        fast = head.next  # move two steps
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next  # move one step
            fast = fast.next.next  # move two steps
        return True

    @staticmethod
    def has_cycle_use_hash_table(head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
