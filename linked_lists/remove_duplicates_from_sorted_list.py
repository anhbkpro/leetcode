from typing import Optional
from .linked_list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
