from typing import List, Optional
from linked_lists.linked_list_node import LinkedListNode


class Solution:
    def splitListToParts(
        self, head: Optional[LinkedListNode], k: int
    ) -> List[Optional[LinkedListNode]]:
        ans = [None] * k

        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next

        split_size = size // k
        num_remaining_parts = size % k

        current = head
        for i in range(k):
            new_part = LinkedListNode(0)
            tail = new_part

            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            for j in range(current_size):
                tail.next = LinkedListNode(current.val)
                tail = tail.next
                current = current.next
            ans[i] = new_part.next

        return ans
