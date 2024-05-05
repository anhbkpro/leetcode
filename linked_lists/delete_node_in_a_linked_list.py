class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        # Overwrite data of next node on current node.
        node.val = node.next.val
        # Make current node point to next of next node.
        node.next = node.next.next
