from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        dummy = None
        carry = 0
        while stack:
            dummy = ListNode(0, dummy)
            curr_val = (stack[-1] * 2 + carry) % 10
            carry = (stack[-1] * 2 + carry) // 10
            dummy.val = curr_val
            stack.pop()

        if carry:
            dummy = ListNode(carry, dummy)

        return dummy
