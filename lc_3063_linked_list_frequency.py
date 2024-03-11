# Definition for singly-linked list.
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def frequencies_of_elements(head: Optional[ListNode]) -> Optional[ListNode]:
        m = defaultdict(int)
        while head:
            m[head.val] = m.get(head.val, 0) + 1
            head = head.next

        dummy = ListNode(0)
        current = dummy
        for v in m.values():
            current.next = ListNode(v)
            current = current.next

        return dummy.next
