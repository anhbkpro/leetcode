from typing import Optional

from linked_lists.linked_list_node import LinkedListNode


class Solution:
    def hasCycle(self, head: Optional[LinkedListNode]) -> bool:
        if head is None:
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
