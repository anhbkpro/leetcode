# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    @staticmethod
    def splitListToParts(root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)
        print(width, remainder)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
