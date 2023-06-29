# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lc_61_rotate_list import ListNode


def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    curr = head
    last = head
    while curr:
        m_count, n_count = m, n
        # traverse m nodes
        while curr and m_count:
            last = curr
            curr = curr.next
            m_count -= 1

        # traverse n nodes
        while curr and n_count:
            curr = curr.next
            n_count -= 1

        # delete n nodes
        last.next = curr

    return head


class Solution:
    pass
