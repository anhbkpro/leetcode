from typing import Optional
from .linked_list_node import LinkedListNode


class Solution:
    def removeNthFromEnd(
        self, head: Optional[LinkedListNode], n: int
    ) -> Optional[LinkedListNode]:
        dummy = LinkedListNode(-1)
        dummy.next = head
        ahead = before = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            ahead = ahead.next
            before = before.next

        before.next = before.next.next
        return dummy.next
