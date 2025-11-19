from typing import List, Optional

from linked_lists.linked_list_node import LinkedListNode


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[LinkedListNode]
    ) -> Optional[LinkedListNode]:
        nums = set(nums)
        dummy = LinkedListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
