from typing import Optional
from .linked_list_node import LinkedListNode


class Solution:
    def middleNode(self, head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
