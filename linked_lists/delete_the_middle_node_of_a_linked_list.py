from typing import Optional
from .linked_list_node import LinkedListNode


class Solution:
    def deleteMiddle(self, head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
        if not head or not head.next:
            return head

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
