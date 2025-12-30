from typing import Optional

from .linked_list_node import LinkedListNode


class Solution:
    def doubleIt(self, head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        dummy = None
        carry = 0
        while stack:
            dummy = LinkedListNode(0, dummy)
            curr_val = (stack[-1] * 2 + carry) % 10
            carry = (stack[-1] * 2 + carry) // 10
            dummy.val = curr_val
            stack.pop()

        if carry:
            dummy = LinkedListNode(carry, dummy)

        return dummy
